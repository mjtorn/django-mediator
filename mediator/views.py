# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.http import HttpResponse

from mediator import forms as mediator_forms

def incoming_message(request):
    """
    """

    type_ = request.POST.get('type', 'sms')
    if type_ == 'mms':
        raise NotImplementedError('MMS not supported yet')
    elif type_ == 'receipt':
        return incoming_receipt(request)

    return incoming_sms(request)

def incoming_sms(request):
    data = request.POST.copy() or None
    if data is not None and not data.has_key('type'):
        data['type'] = 'sms'

    sms_form = mediator_forms.SmsForm(data)

    sms = None
    if sms_form.is_bound and sms_form.is_valid():
        sms = sms_form.save()

    context = {
        'sms_form': sms_form,
        'sms': sms,
    }

    return context

def incoming_receipt(request):
    data = request.POST.copy() or None
    receipt_form = mediator_forms.DeliveryReceiptForm(data)

    receipt = None
    if receipt_form.is_bound and receipt_form.is_valid():
        receipt = receipt_form.save()

    context = {
        'receipt_form': receipt_form,
        'receipt': receipt,
    }

    return context

# EOF


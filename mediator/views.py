# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.http import HttpResponse

from mediator import forms as mediator_forms

def incoming_message(request):
    """
    """

    type_ = request.POST.get('type', 'sms')
    if type_ == 'mms':
        raise NotImplementedError('MMS not supported yet')

    return incoming_sms(request)

def incoming_sms(request):
    data = request.POST.copy() or None
    sms_form = mediator_forms.SmsForm(data)

    sms = None
    if sms_form.is_bound and sms_form.is_valid():
        sms = sms_form.save()

    context = {
        'sms_form': sms_form,
        'sms': sms,
    }

    return context

# EOF


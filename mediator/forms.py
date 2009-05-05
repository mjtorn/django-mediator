# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django import forms

from mediator import models as mediator_models

class SmsForm(forms.ModelForm):
    class Meta:
        model = mediator_models.Sms

class DeliveryReceiptForm(forms.ModelForm):
    class Meta:
        model = mediator_models.DeliveryReceipt

# EOF


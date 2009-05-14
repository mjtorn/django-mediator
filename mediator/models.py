# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.db import models

class Sms(models.Model):
    """Model conforming to Lapitor Mediator's incoming SMS
    """

    created_at = models.DateTimeField(auto_now_add=True)

    # Don't be too strict with fields because we don't know what they are
    command = models.TextField()
    argument = models.TextField(null=True, blank=True)
    numberfrom = models.TextField()
    numberto = models.TextField()
    operator = models.TextField()
    transactionid = models.IntegerField(db_index=True)
    sms = models.TextField()

    # But this is the real content
    @property
    def content(self):
        return '%s %s' % (self.command, self.argument)

    def __unicode__(self):
        return '%s -> %s: %s %s' % (self.numberfrom, self.numberto, self.command, self.argument)


class ReturnSms(models.Model):
    """Model for return data
    """

    sms = models.ForeignKey(Sms)

    numberfrom = models.TextField(null=True, blank=True)
    numberto = models.TextField(null=True, blank=True)
    operator = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    delivery_req_url = models.TextField(null=True, blank=True)
    content = models.TextField()
    
    def __unicode__(self):
        return '%s -> %s: %s %s' % (self.numberfrom, self.numberto, self.content)


class ReturnError(models.Model):
    """Model for error
    """

    # In case we have a system error that the sms does't get logged or somethin
    sms = models.ForeignKey(Sms, null=True)

    err_type = models.TextField()
    text = models.TextField()

    def __unicode__(self):
        return '%s error: %s' % (self.err_type, self.text)


class DeliveryReceipt(models.Model):
    """Delivery receipts
    """

    created_at = models.DateTimeField(auto_now_add=True)

    type = models.TextField()
    status = models.IntegerField()
    transactionid = models.IntegerField(db_index=True)

    def __unicode__(self):
        return '%s: %s: %s' % (self.transactionid, self.type, self.status)

# EOF


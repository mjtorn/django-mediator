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


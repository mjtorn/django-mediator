# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.db import models

class Sms(models.Model):
    """Model conforming to Lapitor Mediator's incoming SMS
    """

    # Don't be too strict with fields because we don't know what they are
    command = models.TextField()
    argument = models.TextField()
    numberfrom = models.TextField()
    numberto = models.TextField()
    operator = models.TextField()
    transactionid = models.IntegerField(db_index=True)
    sms = models.TextField()

    # But this is the real content
    content = models.TextField()

    def __unicode__(self):
        return '%s -> %s: %s %s' % (self.numberfrom, self.numberto, self.command, self.argument)

# EOF


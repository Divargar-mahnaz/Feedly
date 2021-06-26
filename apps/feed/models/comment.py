from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Comment'), on_delete=models.CASCADE)
    article = models.ForeignKey('Article', verbose_name='Article', on_delete=models.CASCADE)
    comment = models.TextField(_('Comment'))

    class Meta:
        db_table = 'comment'

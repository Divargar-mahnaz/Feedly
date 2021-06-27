from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.model_handler import FeedlyModel


class Article(FeedlyModel):
    title = models.CharField(_('Title'), max_length=150)
    link = models.URLField(_('Link'))
    description = models.TextField(_('Description'), null=True, blank=True)
    content = models.TextField(_('Content'), null=True, blank=True)
    author = models.CharField(_('Author'), max_length=100, null=True, blank=True)
    feed = models.ForeignKey('Feed', verbose_name=_('Feed'), related_name='articles', on_delete=models.CASCADE)

    class Meta:
        db_table = 'article'

    def __str__(self):
        return "{}:{}".format(self.id, self.title)

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..common import FEED_IMAGE_PATH
from core.model_handler import FeedlyModel


class Feed(FeedlyModel):
    name = models.CharField(_("Name"), max_length=150, unique=True)
    link = models.URLField(_("Link"))
    image = models.ImageField(_("Image"), upload_to=FEED_IMAGE_PATH, null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)

    class Meta:
        db_table = "feed"

    def __str__(self):
        return "{}:{}".format(self.id, self.name)

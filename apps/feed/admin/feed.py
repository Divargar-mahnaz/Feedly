from django.contrib import admin
from django.utils.html import format_html

from ..models import Feed


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'image_tag')

    def image_tag(self, obj):
        return format_html('<img src="{}" width="35px" height="35px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

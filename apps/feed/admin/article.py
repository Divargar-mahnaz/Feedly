from django.contrib import admin

from ..models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'feed_name', 'link')
    list_display_links = ('title',)
    search_fields = ('feed__name',)

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        return qs.order_by('feed__name')

    @staticmethod
    def feed_name(obj):
        return obj.feed.name

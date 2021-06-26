from django.contrib import admin

from ..models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'comment']
    list_display_links = ['user']

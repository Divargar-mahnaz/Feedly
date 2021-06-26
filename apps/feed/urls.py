from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserFeedsAPIView.as_view(), name='user_feeds'),
    path('scrapy', views.ArticleScrapyAPIView.as_view(), name='article_scrapy')
]

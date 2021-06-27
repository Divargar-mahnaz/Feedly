from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserFeedsAPIView.as_view(), name='user_feeds'),
    path('follow/<int:pk>', views.FollowFeedAPIView.as_view(), name='follow_feed'),
    path('scrapy', views.ArticleScrapyAPIView.as_view(), name='article_scrapy'),
    path('read/<int:pk>', views.ReadArticleAPIView.as_view(), name='read_article'),
    path('<int:pk>/unread', views.UnReadArticlesAPIView.as_view(), name='read_article'),
    path('article/<int:pk>/comment', views.LeaveCommentAPIView.as_view(), name='leave_comment'),
    path('article/<int:pk>/like', views.LikeArticle.as_view(), name='like')
]

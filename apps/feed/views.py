from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.view_handler import ListView, UserAPIView
from .exceptions import FeedNotRegister
from .models import Feed, Article, Comment
from .serializer.article import ArticleSerializer
from .serializer.comment import CommentSerializer
from .serializer.feed import UserFeedsSerializer
from .tasks import article_scrapy


class ArticleScrapyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        feed = Feed.objects.filter(name=request.data.get('feed', None))
        if feed:
            request.data['feed'] = feed[0].id
        ArticleSerializer(data=request.data).is_valid(raise_exception=True)
        article_scrapy.delay(**request.data)
        return Response(data={'message': 'Data Add To Queue'}, status=status.HTTP_200_OK)


class AllFeedsAPIView(ListView):
    serializer_class = UserFeedsSerializer
    queryset = Feed.objects.all()


class UserFeedsAPIView(ListView, UserAPIView):
    serializer_class = UserFeedsSerializer

    def get_queryset(self):
        return self.request.user.feeds.all()


class ReadArticleAPIView(RetrieveAPIView, UserAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.feeds.filter(pk=self.get_object().feed.id):
            request.user.read_articles.add(self.get_object())
        return super().get(request, *args, **kwargs)


class UnReadArticlesAPIView(UserAPIView):
    def get(self, request, *args, **kwargs):
        feed = request.user.feeds.filter(pk=kwargs['pk'])
        if feed:
            unread = feed[0].articles.count() - request.user.read_articles.filter(feed__pk=kwargs['pk']).count()
            return Response({
                'unread': unread
            })
        raise FeedNotRegister


class LeaveCommentAPIView(CreateAPIView, UserAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        request.data['article'] = kwargs['pk']
        return self.create(request, *args, **kwargs)


class FollowFeedAPIView(UserAPIView):
    def post(self, request, *args, **kwargs):
        try:
            request.user.feeds.add(kwargs['pk'])
        except IntegrityError:
            raise NotFound
        return Response(status=status.HTTP_201_CREATED)


class LikeArticle(UserAPIView):
    def post(self, request, *args, **kwargs):
        try:
            request.user.liked_articles.add(kwargs['pk'])
        except IntegrityError:
            raise NotFound
        return Response(status=status.HTTP_201_CREATED)

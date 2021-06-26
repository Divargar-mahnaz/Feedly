from rest_framework.generics import CreateAPIView

from .models import Feed
from core.view_handler import ListView, UserAPIView
from .serializer.article import ArticleSerializer
from .serializer.feed import UserFeedsSerializer


class ArticleScrapyAPIView(CreateAPIView):
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        feed = Feed.objects.filter(name=request.data.get('feed', None))
        if feed:
            request.data['feed'] = feed[0].id
        else:
            request.data['feed'] = None
        return self.create(request, *args, **kwargs)


class UserFeedsAPIView(ListView, UserAPIView):
    serializer_class = UserFeedsSerializer

    def get_queryset(self):
        return self.request.user.feeds.all()

from celery import shared_task

from .models import Article
from .serializer.article import ArticleSerializer


@shared_task
def article_scrapy(**kwargs):
    serialized_data = ArticleSerializer(data=kwargs)
    serialized_data.is_valid(raise_exception=True)
    serialized_data.save()

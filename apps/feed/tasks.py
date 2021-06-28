from celery import shared_task

from .serializer.article import ArticleSerializer


@shared_task
def article_scrapy(**kwargs):
    serialized_data = ArticleSerializer(data=kwargs)
    serialized_data.is_valid()
    serialized_data.save()

# for run : celery -A Feedly worker --pool=solo

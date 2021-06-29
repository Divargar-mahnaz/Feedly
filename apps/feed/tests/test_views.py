from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from ..models import Feed, Article, Comment
from ...account.models import User
from rest_framework.authtoken.models import Token


class ViewTests(APITestCase):
    @staticmethod
    def auth_post(email, url, data):
        token, created = Token.objects.get_or_create(user=User.objects.get(email=email))
        client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)
        return client.post(url, data=data, headers={'Authorization': 'Token ' + token.key}, format='json')

    @staticmethod
    def auth_get(email, url):
        token, created = Token.objects.get_or_create(user=User.objects.get(email=email))
        client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)
        return client.get(url, headers={'Authorization': 'Token ' + token.key})

    def setUp(self):
        User.objects.create_user(email='mahnaz.divargar@gmail.com', password='123')
        Feed.objects.create(name='KDnuggets', link='http://kdnuggets.com')
        Article.objects.create(title='Article in KDnuggets', link='http://kdnuggets.com/first_article',
                               feed=Feed.objects.get(pk=1), description='description', content='content', author='alex')

    def test_correct_scrapy(self):
        url = reverse('article_scrapy')
        data = {
            'title': 'test2',
            'link': 'https://dev.to/zagaris/understanding-destructuring-in-javascript-2ce5',
            "feed": "KDnuggets"
        }

        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_fails_scrapy(self):
        url = reverse('article_scrapy')
        data = {
            'title': 'test2',
            'link': 'https://dev.to/zagaris/understanding-destructuring-in-javascript-2ce5'
        }

        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_view_user_feeds(self):
        url = reverse('user_feeds')
        response = self.auth_get('mahnaz.divargar@gmail.com', url)
        self.assertEqual(response.status_code, 200)

    def test_leave_comment_view(self):
        url = reverse('leave_comment', args=(1,))
        data = {
            'comment': 'add comment for article 1',
        }
        response = self.auth_post('mahnaz.divargar@gmail.com', url, data)
        print(Comment.objects.get(user=1, article=1))
        self.assertEqual(Comment.objects.get(user=1, article=1).comment, 'add comment for article 1')

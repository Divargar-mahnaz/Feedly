from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from ..models import Feed
from ...account.models import User
from rest_framework.authtoken.models import Token


class ViewTests(APITestCase):
    def setUp(self):
        Feed.objects.create(name='KDnuggets', link='http://kdnuggets.com')
        User.objects.create_user(email='mahnaz.divargar@gmail.com', password='123')

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
        token, created = Token.objects.get_or_create(user=User.objects.get(email='mahnaz.divargar@gmail.com'))
        client = APIClient(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get(url, headers={'Authorization': 'Token ' + token.key})
        self.assertEqual(response.status_code, 200)

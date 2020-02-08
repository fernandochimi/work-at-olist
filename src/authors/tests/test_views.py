from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AuthorViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('authors')
        self.user = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_01_list_authors(self):
        "Authors data must be listed"
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_02_filter_authors(self):
        "Authors data must be filtered"
        response = self.client.get(self.url, {'name': 'author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

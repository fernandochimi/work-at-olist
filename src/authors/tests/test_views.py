from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthorViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('authors')

    def test_01_list_authors(self):
        "Authors data must be listed"
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

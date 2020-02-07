from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BookViewTest(APITestCase):
    def setUp(self):
        self.list_url = reverse('book-list')

    def test_01_list_books(self):
        "Books data must be listed"
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_02_filter_books(self):
        "Books data must be filtered"
        response = self.client.get(
            self.list_url,
            {
                'name': 'book',
                'authors': 'author'
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

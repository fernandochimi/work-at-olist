from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.tests.factories import AuthorFactory
from books.tests.factories import BookFactory


class BookViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('books')
        self.authors_factory = AuthorFactory()
        self.book = BookFactory(authors=[self.authors_factory])

    def test_01_list_books(self):
        "Books data must be listed"
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_02_filter_books(self):
        "Books data must be filtered"
        response = self.client.get(
            self.url,
            {
                'name': 'book',
                'authors': 'author'
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_03_create_books(self):
        "Book must be created"
        response = self.client.post(
            self.url,
            {
                'name': self.book.name,
                'edition': self.book.edition,
                'publication_year': self.book.publication_year,
                'authors': self.authors_factory.id
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

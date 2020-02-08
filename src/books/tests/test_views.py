from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authors.tests.factories import AuthorFactory
from books.tests.factories import BookFactory


class BookViewTest(APITestCase):
    def setUp(self):
        self.authors_factory = AuthorFactory()
        self.book = BookFactory(authors=[self.authors_factory])

    def test_01_list_books(self):
        "Books data must be listed"
        response = self.client.get(reverse('books'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_02_filter_books(self):
        "Books data must be filtered"
        response = self.client.get(
            reverse('books'),
            kwargs={
                'name': 'book',
                'authors': 'author',
                'publication_year': 2000,
                'edition': 1
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_03_create_books(self):
        "Book must be created"
        response = self.client.post(
            reverse('books'),
            data={
                'name': self.book.name,
                'edition': self.book.edition,
                'publication_year': self.book.publication_year,
                'authors': self.authors_factory.id
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # TODO: Alter Books test
    # def test_04_alter_books(self):
    #     "Book must be altered"
    #     response = self.client.put(
    #         reverse('books-detail', kwargs={'pk': self.book.pk}),
    #         data={
    #             'name': 'New Book',
    #             'edition': self.book.edition,
    #             'publication_year': self.book.publication_year,
    #             'authors': [{'name': self.authors_factory.name}]
    #         })
    #     print("FAIL: ", response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_05_delete_books(self):
        "Book must be deleted"
        response = self.client.delete(
            reverse('books-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_06_retrieve_book(self):
        "Book must be retrieved"
        response = self.client.get(
            reverse('books-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.test import TestCase

from authors.tests.factories import AuthorFactory
from books.tests.factories import BookFactory


class BookModelsTest(TestCase):
    def setUp(self):
        self.authors_factory = AuthorFactory()
        self.book = BookFactory(authors=[self.authors_factory])

    def test_01_unicode(self):
        "Book description must be a unicode"
        authors_list = ", ".join(
            str(author) for author in self.book.authors.all())
        self.assertEqual(
            str(self.book),
            u"{}, {}, {}".format(self.book.name, self.book.publication_year,
                                 authors_list))

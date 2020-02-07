from django.test import TestCase

from authors.models import Author
from authors.tests.factories import AuthorFactory


class AuthorModelsTest(TestCase):
    def setUp(self):
        self.author = AuthorFactory()

    def test_01_unicode(self):
        "Author name must be a unicode"
        self.assertEqual(str(self.author), u"{}".format(self.author.name))

    def test_02_author_table(self):
        "Authors table must be required one register"
        author_qty = Author.objects.all()
        self.assertTrue(len(author_qty) > 0)

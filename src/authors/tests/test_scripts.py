from django.test import TestCase

from authors.models import Author
from authors.scripts import import_authors


class ImportAuthorsTest(TestCase):
    def setUp(self):
        self.import_authors = import_authors
        self.authors = Author.objects.all()

    def teardown_class(self):
        "Authors table must be cleaned"
        self.authors.delete()
        self.assertTrue(len(self.authors) == 0)

    def test_01_import_authors_csv(self):
        "List of authors must be imported to database"
        author_script = self.import_authors.run('config/authors.csv')
        self.assertEqual(len(self.authors), 6)
        self.assertEqual(author_script, "Import data with success")

    def test_02_import_authors_exception(self):
        "Authors script must show an error"
        with self.assertRaises(Exception) as e:
            self.import_authors.run()
        self.assertIs(Exception, e.expected)
        self.assertTrue('positional argument' in str(e.exception))

import factory
from factory import Sequence, django

from books.models import Book


class BookFactory(django.DjangoModelFactory):
    class Meta:
        model = Book

    name = Sequence(lambda n: u"Book %s" % n)
    edition = 1
    publication_year = 2000

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)

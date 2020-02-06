from factory import Sequence, django

from authors.models import Author


class AuthorFactory(django.DjangoModelFactory):
    class Meta:
        model = Author

    name = Sequence(lambda n: u"Author %s" % n)

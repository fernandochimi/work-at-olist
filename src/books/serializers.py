from django.http import Http404
from rest_framework import serializers

from authors.models import Author
from authors.serializers import AuthorSerializer
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']

    def update(self, instance, data):
        authors_data = data.pop('authors')

        instance.name = data.get('name', instance.name)
        instance.edition = data.get('edition', instance.edition)
        instance.publication_year = data.get(
            'publication_year', instance.publication_year)

        for author in authors_data:
            author_queryset = Author.objects.filter(
                name__exact=author.get('name', None))
            if author_queryset.exists():
                author = author_queryset.first()
            else:
                raise Http404
            instance.authors.add(author)

        instance.save()
        return instance


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']

    def create(self, data):
        authors = data.pop('authors')
        instance = Book.objects.create(**data)
        for author in authors:
            instance.authors.add(author)
        return instance

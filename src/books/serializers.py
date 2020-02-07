from rest_framework import serializers

from authors.serializers import AuthorSerializer
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']


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

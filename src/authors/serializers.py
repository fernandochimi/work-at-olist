from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

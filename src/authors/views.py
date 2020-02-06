from rest_framework.views import APIView
from rest_framework.response import Response

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        author_serializer = AuthorSerializer(authors, many=True)
        return Response(author_serializer.data)
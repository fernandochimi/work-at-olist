from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorListView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

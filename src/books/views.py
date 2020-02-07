from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from books.models import Book
from books.serializers import BookSerializer, BookCreateSerializer


class BookListView(ListCreateAPIView):
    pagination_class = PageNumberPagination
    serializer_class = BookSerializer

    def filter_results(self, params, queryset):
        name = params.get('name', None)
        authors = params.get('authors', None)
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        if authors is not None:
            queryset = queryset.filter(authors__name__contains=authors)
        return queryset

    def get_queryset(self):
        queryset = Book.objects.all()
        query_params = self.request.query_params
        if query_params is not None and len(query_params) > 0:
            queryset = self.filter_results(query_params, queryset)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        return BookSerializer

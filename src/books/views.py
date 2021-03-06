from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer, \
    BookCreateSerializer


class BookListView(ListCreateAPIView):
    pagination_class = PageNumberPagination
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def filter_results(self, params, queryset):
        name = params.get('name', None)
        edition = params.get('edition', None)
        publication_year = params.get('publication_year', None)
        authors = params.get('authors', None)

        if name is not None:
            queryset = queryset.filter(name__contains=name)

        if edition is not None:
            queryset = queryset.filter(edition__contains=edition)

        if publication_year is not None:
            queryset = queryset.filter(
                publication_year__contains=publication_year)

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


class BookDetailView(RetrieveUpdateDestroyAPIView):
    pagination_class = PageNumberPagination
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()

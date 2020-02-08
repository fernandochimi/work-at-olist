from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorListView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Author.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        return queryset

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from authors import views as authors_views
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', authors_views.AuthorListView.as_view(), name='authors'),
    path('books/', books_views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/',
         books_views.BookDetailView.as_view(), name='books-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

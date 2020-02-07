from django.db import models

from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=255)
    edition = models.PositiveIntegerField()
    publication_year = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['-publication_year', 'name']

    def __str__(self):
        authors_list = ", ".join(
            str(author) for author in self.authors.all())
        return '{}, {}, {}'.format(self.name, self.publication_year,
                                   authors_list)

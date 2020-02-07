from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ['name']

    def __str__(self):
        return self.name

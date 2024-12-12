from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    class Meta:
        app_label = 'api'
    name = models.CharField(max_length=200)


class Book(models.Model):
    class Meta:
        app_label = 'api'
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"

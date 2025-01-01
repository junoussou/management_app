from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)  # Titre du livre
    author = models.CharField(max_length=100)  # Auteur
    published_date = models.DateField()  # Date de publication

    def __str__(self):
        return self.title

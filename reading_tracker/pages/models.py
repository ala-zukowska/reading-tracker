from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

class Author(models.Model):
    first_name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    def __str__(self):
            return f"{self.first_name} {self.surname}"

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return self.title

class Private_Note(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note_text = models.TextField()
    def __str__(self):
            return self.note_text
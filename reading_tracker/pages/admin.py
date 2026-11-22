from django.contrib import admin

from .models import Book, Author, Private_Note

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Private_Note)
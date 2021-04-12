from books.models import Author, Book, Category, Genre, Tag
from django.contrib import admin

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Tag)
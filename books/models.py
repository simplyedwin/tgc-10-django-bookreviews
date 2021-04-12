# A model is the single, definitive source of information about your data. 
# It contains the essential fields and behaviors of the data you’re storing. 
# Generally, each model maps to a single database table.

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Genre (models.Model):
    genre = models.CharField(blank=False, max_length=255)

    def __str__(self) -> str:
        return self.genre


class Category(models.Model):
    category = models.CharField(blank=False, max_length=255)

    def __str__(self) -> str:
        return self.category


class Tag (models.Model):
    tag = models.CharField(blank=False, max_length=255)

    def __str__(self) -> str:
        return self.tag


class Author (models.Model):
    FirstName = models.CharField(blank=False, max_length=255)
    LastName = models.CharField(blank=False, max_length=255)
    DateOfBirth = models.DateTimeField()
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.FirstName + " " + self.LastName


class Book (models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title

from books.models import Book
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.reverse_related import ManyToOneRel
from django.contrib.auth.models import User



# Create your models here.
class Review(models.Model):
    title = models.CharField(blank=False,max_length=255)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    content = models.CharField(blank=False,max_length=255)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    
    def __str__(self) -> str:
        return self.title
from django import forms
from django.forms import fields
from .models import Author, Book

# class BookForm inherits all data and functionality from forms.ModelForm superclass


class BookForm(forms.ModelForm):
    # define which model the form is for inside the Meta class
    class Meta:
        model = Book
        # define the fields from the model that are to be shown on the form,
        # must be same as defined in models.py for Book Model
        fields = {'title', 'desc', 'ISBN', 'genre', 'category', 'tags','authors','owner'}
        # fields = {'title', 'desc', 'ISBN', 'genre', 'category'}
        # fields = {'title', 'desc', 'ISBN', 'genre', 'category', 'tags'}




class AuthorForm(forms.ModelForm):
    # define which model the form is for inside the Meta class
    class Meta:
        model = Author
        fields = {'FirstName', 'LastName', 'DateOfBirth','owner'}

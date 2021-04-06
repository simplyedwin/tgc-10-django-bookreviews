from django import forms
from django.forms import fields
from .models import Author, Book

#class BookForm inherits all data and functionality from forms.ModelForm superclass
class BookForm(forms.ModelForm):
    # define which model the form is for inside the Meta class
    class Meta:
        model = Book
        fields = {'title','desc','ISBN'} # define the fields from the model that are to be shown on the form

class AuthorForm(forms.ModelForm):
    # define which model the form is for inside the Meta class
    class Meta:
        model = Author
        fields = {'FirstName','LastName','DateOfBirth'}
from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Author, Book
from .forms import AuthorForm, BookForm
# Create your views here.


def index(request):
    # return HttpResponse("Books app")
    books = Book.objects.all()

    # pass the books to the template file in the templates/books folder
    return render(request, "books/index-template.html", {'books': books})


def index_author(request):
    authors = Author.objects.all()

    # pass the authors to the template file in the templates/books folder
    return render(request, 'books/author-template.html', {'authors': authors})


def create_book(request):

    if request.method == 'POST':
        create_form = BookForm(request.POST)

        # check if the form is valid
        if create_form.is_valid():
            create_form.save()
            # redirect back to index view function
            return redirect(reverse(index))
        else:
            # if form is invalid, re-enter the form
            return render(request, 'books/create-template.html', {
                'form': create_form
            })

    else:
        create_form = BookForm()
        return render(request, 'books/create-template.html', {
            'form': create_form
        })


def create_author(request):

    if request.method == 'POST':
        create_form = AuthorForm(request.POST)

        # check if the form is valid
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index_author))
        else:
            return render(request, 'books/create-template.html', {'form': create_form})

    else:

        create_form = AuthorForm()
        return render(request, 'books/create-template.html', {'form': create_form})

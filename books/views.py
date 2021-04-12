# to import flash messages
from django.contrib import messages

# to allow logged in user to perform CRUD operation
from django.contrib.auth.decorators import login_required, permission_required

from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Author, Book
from .forms import AuthorForm, BookForm
from reviews.forms import ReviewForm
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

# this decorator is needed to ensure login is required before accessing this view function (i.e create a book)


@login_required
def create_book(request):

    if request.method == 'POST':
        create_form = BookForm(request.POST)

        # check if the form is valid
        if create_form.is_valid():
            create_form.save()

            messages.success(
                request, f"New Book {create_form.cleaned_data['title']} has been created")

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
            messages.success(
                request, f"New Author {create_form.cleaned_data['FirstName']} {create_form.cleaned_data['LastName']} has been created")
            return redirect(reverse(index_author))
        else:
            return render(request, 'books/create-template.html', {'form': create_form})

    else:

        create_form = AuthorForm()
        return render(request, 'books/create-template.html', {'form': create_form})


def update_book(request, book_id):
    # retrieve the book which we are updating
    book_being_updated = get_object_or_404(Book, pk=book_id)
    

    # if the update form is submitted
    if request.method == 'POST':

        # create the form and fill in the user's data. Also specify that this is to
        # update an existing model (the instance arguement)
        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            book_form.save()
            messages.info(
                request, f"{book_form.cleaned_data['title']} has been updated")
            return redirect(reverse(index))
        else:
            render(
                request, 'books/update-template.html', {'form': book_form}
            )
    else:

        # create a form with the book details filled in
        book_form = BookForm(instance=book_being_updated)
        return render(
            request, 'books/update-template.html', {'form': book_form}
        )

    # create the form and fill it with data from book instance
    book_form = BookForm(instance=book_being_updated)

    return render(request, 'books/update-template.html', {'form': book_form})


def update_author(request, author_id):

    author_being_updated = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        author_form = AuthorForm(request.POST, instance=author_being_updated)
        if author_form.is_valid():
            author_form.save()
            messages.error(
                request, f" {author_form.cleaned_data['FirstName']} {author_form.cleaned_data['LastName']} has been updated")

            return redirect(reverse(index_author))
        else:
            return render(request, 'books/update-template.html', {'form': author_form})

    else:

        author_form = AuthorForm(instance=author_being_updated)
        return render(request, 'books/update-template.html', {'form': author_form})


def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, pk=book_id
                                       )
    if request.method == 'POST':
        book_to_delete.delete()
        messages.warning(
                request, f"{book_to_delete.title} has been deleted")
        return redirect(reverse(index))
    else:
        return render(request, 'books/delete-template.html', {'book': book_to_delete})


def delete_author(request, author_id):
    author_to_delete = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        author_to_delete.delete()
        messages.warning(
                request, f" {author_to_delete.FirstName} {author_to_delete.LastName} has been deleted")
        return redirect(reverse(index_author))
    else:

        return render(request, 'books/delete-template.html', {'author': author_to_delete})

def view_book_details(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    review_form = ReviewForm()
    return render(request,'books/details-template.html',{'book':book,'form':review_form})

    
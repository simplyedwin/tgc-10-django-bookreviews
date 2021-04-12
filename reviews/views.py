from django.contrib import messages
from reviews.forms import ReviewForm
from reviews.models import Review
from django.shortcuts import get_object_or_404, redirect, render, reverse, HttpResponse
from books.models import Book

# Create your views here.


def index(request):

    reviews = Review.objects.all()
    # return HttpResponse("Welcome to reviews")
    return render(request, "reviews/index-template.html", {'reviews': reviews})


def create_review(request, book_id):

    if request.method == "POST":

        create_form = ReviewForm(request.POST)

        if create_form.is_valid():
            
            # The commit=false optional parameter is passed to the form.save() function. 
            # This will create a new instance of Review using the data in the POST request, 
            # but won't save to the database yet so that we can assign the user to the review.
            review = create_form.save(commit=False)
            
            # To access the current user by referring to the user object inside the request object. 
            # When the review is added, we will assign the current logged 
            # in user to the user variable in the Review object.
            review.user = request.user
            review.book = get_object_or_404(Book,pk=book_id)
            review.save()

            messages.success(
                request, f"New Book Review, {create_form.cleaned_data['title']}, has been created")

            return redirect(reverse(index))
        else:
            return render(request, 'reviews/create-template.html', {'form': create_form})
    else:

        create_form = ReviewForm()
        return render(request, 'reviews/create-template.html', {'form': create_form})


def update_review(request, review_id):

    review_to_be_updated = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':

        update_form = ReviewForm(request.POST, instance=review_to_be_updated)
        if update_form.is_valid():
            update_form.save()

            messages.info(
                request, f"{update_form.cleaned_data['title']} has been updated")
            return redirect(reverse(index))
        else:
            return render(request, 'reviews/update-template.html', {'form': update_form})
    else:
        update_form = ReviewForm(instance=review_to_be_updated)
        return render(request, 'reviews/update-template.html', {'form': update_form})


def delete_review(request, review_id):

    review_to_be_deleted = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_to_be_deleted.delete()
        messages.warning(
                request, f" {review_to_be_deleted.title} has been deleted")
        return redirect(reverse(index))
    else:
        return render(request, 'reviews/delete-template.html', {'review': review_to_be_deleted})

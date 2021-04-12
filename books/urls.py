"""BookReviewsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import books.views  # must import in the view.py of the app
import reviews.views

# routing path with view functions
urlpatterns = [
    # app folder then view.py then view function
    path('', books.views.index, name='show_book_route'),
    path('create', books.views.create_book),
    path('update/<book_id>', books.views.update_book,
         name='update_book_route'),  # assign a name to the route
    path('delete/<book_id>',
         books.views.delete_book, name='delete_book_route'),
    path('authors/', books.views.index_author, name='show_author_route'),
    path('create/author', books.views.create_author),
    path('update/author/<author_id>', books.views.update_author,
         name='update_author_route'),  # assign a name to the route
    path('delete/author/<author_id>',
         books.views.delete_author, name='delete_author_route'),
    path('view/<book_id>', books.views.view_book_details, name = 'view_book_details')
]

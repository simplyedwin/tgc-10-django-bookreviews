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
from django.urls import path
import books.views # must import in the view.py of the app
import reviews.views

# routing path with view functions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',books.views.index), # app folder then view.py then view function
    path('reviews/', reviews.views.index),
    path('authors/',books.views.index_author),
    path('books/create/book',books.views.create_book),
    path('books/create/author',books.views.create_author),

]

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
import books.views # must import in the view.py of the app
import reviews.views

# routing path with view functions
urlpatterns = [
    path('', reviews.views.index,name='show_review_route'),
    path('create/<book_id>', reviews.views.create_review,name='create_review_route'),
    path('update/<review_id>', reviews.views.update_review,name='update_review_route'),
    path('delete/<review_id>', reviews.views.delete_review,name='delete_review_route'),
]

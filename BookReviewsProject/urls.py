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
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')), # url for other accounts to login
    path('books/', include('books.urls')), # url for books app
    path('reviews/', include('reviews.urls')), # url for books app

]

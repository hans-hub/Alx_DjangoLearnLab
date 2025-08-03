from django.contrib import admin
from django.urls import path, include   
from api.views import BookList  # Import the BookList view


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='list_book'),  # FBV
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV
]

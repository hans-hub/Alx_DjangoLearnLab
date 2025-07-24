from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # FBV
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV
    path('register/', views.register_view, name='register'),  # for registration page
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # FBV
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV
    path('login/', views.login_view, name='login'),  # for login page
    path('logout/', views.logout_view, name='logout'),  # for logout page
    path('register/', views.register_view, name='register'),  # for registration page
]

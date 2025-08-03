
from django.contrib import admin
from django.urls import include, path
from my_app import views   
from django.urls import path
from my_app.views import BookListCreateAPIView  
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),
    
]

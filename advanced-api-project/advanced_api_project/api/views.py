from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework import generics,permissions,filters
from .models import Book
from .serializers import BookSerializer 



#List all books (public access)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view
    filterset_fields = ['publication_year', 'author']
    ordering_fields = ['title', 'publication_year']

#enabling filtering, searching and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

#Specidy fields for filtering
filterset_fields = ['title','author','publication_year']

#Fields for searching(search uses `icontains`)
search_fields = ['title', 'author']

# Fields allowed for ordering
ordering_fields = ['title', 'publication_year']
ordering = ['title']  # Default ordering

# Retrieve a specific book by ID (public access)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view


#view for adding books (authenticated users only)
class BookCreateView(generics.CreateAPIView):   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books

    def perform_create(self, serializer):
        print(f"User {self.request.user} is creating a book.")
        serializer.save(author=self.request.user)  # Save the author as the currently logged-in user



# view for updating books (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)  # Save the author as the currently logged-in user

# view for deleting books (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete books

    def perform_destroy(self, instance):
        instance.delete()   
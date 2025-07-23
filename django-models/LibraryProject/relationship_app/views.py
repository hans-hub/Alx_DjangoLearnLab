from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
# Function-based view that displays a list of books with their authors

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})



# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['books'] = self.object.books.select_related('author').all()
        return ctx

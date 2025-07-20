# query_samples.py
import os
import django

# Setup Django env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # 1. Query all books by a specific author
    author = Author.objects.get(name="J. K. Rowling")
    books_by_author = author.books.all()
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # 2. List all books in a library
    library = Library.objects.get(name="Central Library")
    library_books = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in library_books]}")

    # 3. Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian at {library.name}: {librarian.name}")

if __name__ == "__main__":
    sample_queries()
# This script demonstrates how to perform basic queries on the models defined in relationship_app.
# Make sure to run this script in the Django environment where the models are defined.
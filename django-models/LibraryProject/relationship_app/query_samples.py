# query_samples.py
import os
import django

# Setup Django env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # Example variable for the library name
    library_name = "Central Library"

    # ✅ 1. Retrieve the library
    library = Library.objects.get(name=library_name)

    # 2. Query all books in that library
    books_in_library = library.books.all()
    print(f"Books in {library.name}:", [b.title for b in books_in_library])

    # 3. Retrieve the librarian associated with that library
    librarian = library.librarian
    print(f"Librarian at {library.name}:", librarian.name)

    4.#Query book by specific author
    author_name = "J.K. Rowling"
    books_by_author = Book.objects.filter(author__name=author_name)     
    print(f"Books by {author_name}:", [b.title for b in books_by_author])   


if __name__ == "__main__":
    sample_queries()
# This script demonstrates how to perform basic queries on the models defined in relationship_app.
# Make sure to run this script in the Django environment where the models are defined.
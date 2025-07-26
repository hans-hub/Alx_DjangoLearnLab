from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

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




# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')  # Replace 'home' with your actual home page route name
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')



def role_required(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(decorator)

@login_required
@role_required('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@role_required('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@role_required('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

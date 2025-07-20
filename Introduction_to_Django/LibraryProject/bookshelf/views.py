from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Fucntion-based view that displays a simple message 

def hello_view(request):
    """A simple view that returns a greeting."""
    return HttpResponse("Hello, welcome to the bookshelf app!")


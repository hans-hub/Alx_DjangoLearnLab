from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Book    
from .serializers import BookSerializer 



class BookList(generics.ListAPIView):    
    queryset = Book.objects.all()
    serializer_class = BookSerializer   

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

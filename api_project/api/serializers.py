from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # or specify fields like ['id', 'title', 'author', 'published_date', 'isbn']
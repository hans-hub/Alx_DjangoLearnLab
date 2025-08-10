
from rest_framework import serializers
from .models import Book,Author
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # or specify fields like ['id', 'title', 'author', 'published_date', 'isbn']



    def validate_publication_year(self,value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# This serializer will convert the Book model instances into JSON format and vice versa.

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']  
# This is an author serializer.



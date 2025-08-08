from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        

class AuthorSerializer(serializers.ModelSerializer):
    
    
    publicationyear = AuthorSerializer(many=True, read_only=True)
    class Meta:
   
        model = Author
        fields = ['name', 'publication_year']
        
    def validate(self, data):
        if len(data['publication_year']) > 2025:
            raise serializers.ValidationError("year cannot be in the future")
        return data
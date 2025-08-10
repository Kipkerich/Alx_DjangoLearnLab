from django.shortcuts import render
from rest_framework import generics
from .models import Book 
from .serializers import BookSerializer

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class DetailVIew(generics.ListAPIView):
    queryset = Book.objects.get()
    serializer_class = BookSerializer
    
class CreateView(generics.CreateAPIView):
    new_book = Book(title=input(), author=input(), puplicationyear=input())

    new_book.save()    

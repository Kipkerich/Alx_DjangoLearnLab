from django.shortcuts import render
from rest_framework import generics
from .models import Book 
from .serializers import BookSerializer

class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def DetailView(self):
        author = self.request.author
        return Book.objects.filter(Book=author)
    
    def CreateView(self):
        pass
    
    def UpdateView(self):
        pass
    
    def DeleteView(self):
        pass
    
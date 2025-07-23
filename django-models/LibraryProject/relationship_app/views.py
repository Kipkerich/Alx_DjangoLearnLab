from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all() #Fetch all book instances from the database
    context = {'book_list': books}
    
    return render(request, books/list_books.html , context)


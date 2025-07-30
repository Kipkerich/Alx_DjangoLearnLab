from django.shortcuts import render
from django.contrib.auth.models import Permission
from .models import Book


@Permission('bookshelf.can_edit', raise_exception=True)

class BookAdmin(Book):
    try:
        book_list = ("title")
        
    except: 
        PermissionError('Do not have permission to execute this command')
    
        
    
    

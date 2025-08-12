from django.urls import path
from .views import *

urlpatterns =[
    path('books/', DetailView, name='get_books'),
    path('books/create', CreateView, name='post_books'),
    path('books/update', UpdateView, name='put_book'),
    path('books/delete', DeleteView, name='delete_book'),
    path('books/<int:pk>', DetailView, name='book_details'),
]
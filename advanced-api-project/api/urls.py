from django.urls import path
from .views import *

urlpatterns =[
    path('books/', DetailView, name='get_books'),
    path('books/create', CreateView, name='post_books'),
    path('books/<int:pk>', DetailView, name='booK-details'),
]
from django.db import models

class Author(models.Model):
    author =models.CharField(max_length=100)
    
    
class Book(models.Model):
    book = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='writer')
    

from django.contrib import admin
from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'Publication_year')

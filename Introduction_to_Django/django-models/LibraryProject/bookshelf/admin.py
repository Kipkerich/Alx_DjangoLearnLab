from django.contrib import admin
from .models import Book



class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ()
    

admin.site.register(Book)

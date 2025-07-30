from django.contrib import admin
from .models import Book, CustomUser, CustomUserManager



class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ()
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)



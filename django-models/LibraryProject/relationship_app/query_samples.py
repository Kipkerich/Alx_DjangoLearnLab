from .models import *

books_by_author_name = Author.objects.all()

books_in_library = Library.books.objects.all()

librarian = Librarian.objects.all()

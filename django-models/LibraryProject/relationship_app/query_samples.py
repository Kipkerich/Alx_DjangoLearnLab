from .models import *

books_by_author_name = Author.objects.all()

books_in_library = Library.objects.get(name=library_name), Library.books.all()

librarian = Librarian.objects.all()

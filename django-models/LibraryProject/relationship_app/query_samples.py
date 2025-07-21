from .models import *

books_by_author_name = Author.objects.get(name=author_name), objects.filter(author=author)

books_in_library = Library.objects.get(name=library_name), Library.books.all()

librarian = Librarian.objects.all()

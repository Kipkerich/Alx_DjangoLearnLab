from .models import *

books_by_author_name = Author.objects.get(name=Book), Author.objects.filter(author=Author)

books_in_library = Library.objects.get(name=Library), Library.books.all()

librarian = Librarian.objects.get(name=Librarian)

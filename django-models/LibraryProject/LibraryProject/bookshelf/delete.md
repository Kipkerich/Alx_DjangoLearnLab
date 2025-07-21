from bookshelf.models import Book
#Deleting all the books created

book = Book.delete('book.delete')

#Checking if there is any book to retrieve
book = Book.object.get.all()
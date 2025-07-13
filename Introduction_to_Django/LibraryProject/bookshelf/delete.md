#Deleting all the books created

book = Book.object.delete.all()

#Checking if there is any book to retrieve
book = Book.object.get.all()
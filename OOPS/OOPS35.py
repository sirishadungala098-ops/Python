class Book:
    def read(self):
        print("Reading book")
class Library:
    def __init__(self):
        self.book1 = Book()
        self.book2 = Book()
    def read_books(self):
        self.book1.read()
        self.book2.read()
library = Library()
library.read_books()
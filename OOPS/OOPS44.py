class Book:
    def __init__(self, name):
        self.name = name
class SearchService:
    def search(self, book):
        print("Searching for:", book)
class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("HTML")
        ]
    def search_book(self, service, book):
        service.search(book)
library = Library()
search = SearchService()
library.search_book(search, "Python")
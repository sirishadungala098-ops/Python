class Person:
    def __init__(self, name):
        self.name = name
class Member(Person):
    def borrow_book(self, book):
        print(self.name, "borrowed", book.title)
class Book:
    def __init__(self, title):
        self.title = title
class SearchService:
    def search(self, title):
        print("Searching for:", title)
class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java")
        ]
        self.members = [
            Member("Sirisha")
        ]
    def search_book(self, service, title):
        service.search(title)
library = Library()
search = SearchService()
library.search_book(search, "Python")
library.members[0].borrow_book(library.books[0])
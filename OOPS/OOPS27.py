class SearchService:
    def search(self, book):
        print("Searching for:", book)
class Library:
    def find_book(self, search_service, book):
        search_service.search(book)
library = Library()
search = SearchService()
library.find_book(search, "Python Programming")
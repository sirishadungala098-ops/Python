class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.issued = False
    def issue(self):
        if self.issued == False:
            self.issued = True
            print("Book issued")
        else:
            print("Book already issued")
    def return_book(self):
        self.issued = False
        print("Book returned")
book = LibraryBook("Python")
book.issue()
book.issue()
book.return_book()
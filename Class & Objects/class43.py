class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(self.title)
        print(self.author)
        print(self.price)
b = Book("Python", "John", 500)
b.display()
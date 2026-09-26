class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
b1 = Book("Python", "John", 500)
b2 = Book("Java", "James", 600)
print(b1.title, b1.author, b1.price)
print(b2.title, b2.author, b2.price)
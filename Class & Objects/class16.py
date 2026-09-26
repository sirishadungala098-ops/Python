class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
b1 = Book("Python", "John", 500, 300)
b2 = Book("Java", "James", 600, 400)
print(b1.title, b1.author, b1.price, b1.pages)
print(b2.title, b2.author, b2.price, b2.pages)
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity
p1 = Product("Pen", 10, 5)
p2 = Product("Book", 50, 2)
print(p1.name, p1.total())
print(p2.name, p2.total())
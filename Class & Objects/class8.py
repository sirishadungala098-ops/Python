class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
p1 = Product("Pen", 20, 5)
print(p1.name)
print(p1.price)
print(p1.quantity)
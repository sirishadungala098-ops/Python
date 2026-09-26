class Product:
    def __init__(self, price):
        self.price = price
    def total(self, quantity):
        return self.price * quantity
p = Product(100)
print(p.total(5))
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        print("Total Price:", self.price * self.quantity)
p = Product("Pen", 10, 5)
p.total_price()
class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    def total_cost(self):
        print("Total Cost:", self.price * self.quantity)
p = Product(100, 5)
p.total_cost()
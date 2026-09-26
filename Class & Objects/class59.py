class ShoppingCart:
    def __init__(self):
        self.products = []
    def add(self, product, price):
        self.products.append((product, price))
    def remove(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
    def total(self):
        total = 0
        for item in self.products:
            total = total + item[1]
        return total
cart = ShoppingCart()
cart.add("Pen", 20)
cart.add("Book", 100)
print(cart.total())
cart.remove("Pen")
print(cart.total())
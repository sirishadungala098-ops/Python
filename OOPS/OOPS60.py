class User:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("User:", self.name)
class Customer(User):
    def shop(self):
        print(self.name, "is shopping")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Laptop(Product):
    def display(self):
        print("Laptop:", self.name)
class Mobile(Product):
    def display(self):
        print("Mobile:", self.name)
class ShoppingCart:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart")
    def total_price(self):
        total = 0
        for product in self.products:
            total = total + product.price
        return total
class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "successful")
class DeliveryService:
    def deliver(self):
        print("Order is out for delivery")
class Order:
    def __init__(self, cart):
        self.cart = cart
    def place_order(self, payment, delivery):
        total = self.cart.total_price()
        payment.pay(total)
        delivery.deliver()
customer = Customer("Sirisha")
laptop = Laptop("Dell Laptop", 50000)
mobile = Mobile("Samsung Mobile", 20000)
cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(mobile)
payment = PaymentService()
delivery = DeliveryService()
order = Order(cart)
customer.display()
customer.shop()
laptop.display()
mobile.display()
order.place_order(payment, delivery)
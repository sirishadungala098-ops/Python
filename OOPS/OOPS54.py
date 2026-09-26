class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Laptop(Product):
    pass
class Mobile(Product):
    pass
class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "successful")
class DeliveryService:
    def deliver(self):
        print("Product is out for delivery")
class ShoppingCart:
    def __init__(self):
        self.products = [
            Laptop("Laptop", 50000),
            Mobile("Mobile", 20000)
        ]
    def checkout(self, payment, delivery):
        total = 0
        for product in self.products:
            total = total + product.price
        payment.pay(total)
        delivery.deliver()
cart = ShoppingCart()
payment = PaymentService()
delivery = DeliveryService()
cart.checkout(payment, delivery)
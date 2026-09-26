class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "successful")
class DeliveryService:
    def deliver(self):
        print("Order is out for delivery")
class OnlineOrder:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 1000)
        ]
    def checkout(self, payment, delivery):
        total = 0
        for product in self.products:
            total = total + product.price
        payment.pay(total)
        delivery.deliver()
order = OnlineOrder()
payment = PaymentService()
delivery = DeliveryService()
order.checkout(payment, delivery)
class Order:
    def __init__(self, amount):
        self.amount = amount
class OnlineOrder(Order):
    def place(self):
        print("Online order placed")
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Restaurant:
    def __init__(self):
        self.menu = [
            MenuItem("Pizza", 300),
            MenuItem("Burger", 150)
        ]
class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "successful")
class DeliveryService:
    def deliver(self):
        print("Food is being delivered")
order = OnlineOrder(450)
restaurant = Restaurant()
payment = PaymentService()
delivery = DeliveryService()
order.place()
payment.pay(order.amount)
delivery.deliver()
print("Menu:", restaurant.menu[0].name)
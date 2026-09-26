class PaymentGateway:
    def pay(self, amount):
        print("Payment of", amount, "completed")
class ShoppingCart:
    def checkout(self, gateway):
        gateway.pay(2000)
cart = ShoppingCart()
gateway = PaymentGateway()
cart.checkout(gateway)
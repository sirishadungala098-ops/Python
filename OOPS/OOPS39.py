class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "successful")
class Order:
    def place_order(self, payment_service):
        payment_service.pay(1500)
order = Order()
payment = PaymentService()
order.place_order(payment)
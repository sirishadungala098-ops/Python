class UPIPayment:
    def pay(self):
        print("Payment using UPI")
class CardPayment:
    def pay(self):
        print("Payment using Card")
class CashPayment:
    def pay(self):
        print("Payment using Cash")
payments = [UPIPayment(), CardPayment(), CashPayment()]
for payment in payments:
    payment.pay()
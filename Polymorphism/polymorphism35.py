class UPIPayment:
    def pay(self):
        print("Payment using UPI")
class CardPayment:
    def pay(self):
        print("Payment using Card")
def process_payment(payment):
    payment.pay()
process_payment(UPIPayment())
process_payment(CardPayment())
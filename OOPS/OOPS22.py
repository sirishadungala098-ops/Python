class PaymentService:
    def make_payment(self, amount):
        print("Payment of", amount, "processed")
class BankAccount:
    def pay_bill(self, payment_service):
        payment_service.make_payment(500)
account = BankAccount()
service = PaymentService()
account.pay_bill(service)
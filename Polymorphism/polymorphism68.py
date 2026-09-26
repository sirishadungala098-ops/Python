class UPI:
    def pay(self, amount):
        print("Payment of", amount, "made using UPI")
class Card:
    def pay(self, amount):
        print("Payment of", amount, "made using Card")
class NetBanking:
    def pay(self, amount):
        print("Payment of", amount, "made using Net Banking")
payment_methods = [UPI(), Card(), NetBanking()]
for payment in payment_methods:
    payment.pay(2000)
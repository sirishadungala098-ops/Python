from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment")

class Card(Payment):
    def pay(self):
        print("Card Payment")

payments = [UPI(), Card()]

for payment in payments:
    payment.pay()
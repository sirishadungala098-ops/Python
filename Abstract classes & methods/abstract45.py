from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Amount: 2,000")


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")


p = UPI()
p.pay()
p.display_amount()
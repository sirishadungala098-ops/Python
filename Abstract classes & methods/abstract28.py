from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, id):
        self.amount = amount
        self.id = id

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI Payment:", self.amount)

class Card(Payment):
    def pay(self):
        print("Card Payment:", self.amount)

UPI(1000, 101).pay()
Card(2000, 102).pay()
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, number):
        self.holder = holder
        self.number = number

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Interest: 5%")

a = SavingsAccount("Sirisha", 101)
a.calculate_interest()
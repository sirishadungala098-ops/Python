from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    @abstractmethod
    def display(self):
        pass

class SavingsAccount(Account):
    def display(self):
        print("Savings:", self.balance)

class CurrentAccount(Account):
    def display(self):
        print("Current:", self.balance)

SavingsAccount(101, 5000).display()
CurrentAccount(102, 10000).display()
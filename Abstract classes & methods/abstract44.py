from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Balance: 10,000")


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Interest: 500")


a = SavingsAccount()
a.calculate_interest()
a.display_balance()
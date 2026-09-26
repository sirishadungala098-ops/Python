class Customer:
    def __init__(self, name):
        self.name = name
class PaymentService:
    def pay(self, amount):
        print("Payment of", amount, "completed")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount, payment):
        if amount <= self.balance:
            self.balance = self.balance - amount
            payment.pay(amount)
        else:
            print("Insufficient balance")
class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account interest is 5%")
class CurrentAccount(BankAccount):
    def interest(self):
        print("Current account interest is 2%")
class Bank:
    def __init__(self):
        self.customers = [
            Customer("Sirisha")
        ]
        self.accounts = [
            SavingsAccount(10000),
            CurrentAccount(20000)
        ]
bank = Bank()
payment = PaymentService()
bank.accounts[0].interest()
bank.accounts[0].withdraw(2000, payment)
class BankAccount:
    def deposit(self):
        print("Money deposited")
class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account gives interest")
class CurrentAccount(BankAccount):
    def business(self):
        print("Current account is used for business")
savings = SavingsAccount()
current = CurrentAccount()
savings.deposit()
savings.interest()
current.deposit()
current.business()
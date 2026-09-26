class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)
    def withdraw(self, amount):
        self.balance -= amount
        print("Balance:", self.balance)
a = BankAccount(10000)
a.deposit(2000)
a.withdraw(3000)
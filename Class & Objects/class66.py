class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")
a = BankAccount(5000)
a.withdraw(2000)
a.withdraw(4000)
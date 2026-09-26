class BankAccount:
    def calculate_interest(self):
        print("Calculating interest")
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account interest: 5%")
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account interest: 2%")
accounts = [SavingsAccount(), CurrentAccount()]
for account in accounts:
    account.calculate_interest()
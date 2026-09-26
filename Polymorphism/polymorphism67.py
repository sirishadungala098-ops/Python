class SavingsAccount:
    def calculate_interest(self, amount):
        return amount * 0.05
class CurrentAccount:
    def calculate_interest(self, amount):
        return amount * 0.02
class FixedDeposit:
    def calculate_interest(self, amount):
        return amount * 0.07
accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDeposit()
]
for account in accounts:
    print("Interest:", account.calculate_interest(10000))
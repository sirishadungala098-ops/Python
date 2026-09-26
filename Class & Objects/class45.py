class BankAccount:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance
a = BankAccount("Sirisha", 12345, 10000)
print(a.holder)
print(a.number)
print(a.balance)
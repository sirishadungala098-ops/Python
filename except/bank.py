balance=5000
try:
    amount=int(input("Enter the amount to withdraw: "))
    if amount<=0:
        raise ValueError("withdrawal amount must be greater than zero")
    if amount>balance:
        raise ValueError("insufficient balance")
    balance=balance-amount
    print(balance)
except ValueError as e:
    print("transaction failed:",e)


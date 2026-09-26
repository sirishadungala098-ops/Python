balance = 5000
try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance = balance - amount
    print("Withdrawal successful")
    print("Balance:", balance)
except ValueError as e:
    print(e)
finally:
    print("Transaction completed")
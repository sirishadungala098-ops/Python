try:
    age = int(input("Enter your age: "))
    if age > 18:
        raise ValueError("you are eligible to vote")
except ValueError as e:
    print("Error:", e)
else:
    print("you are not eligible to vote")

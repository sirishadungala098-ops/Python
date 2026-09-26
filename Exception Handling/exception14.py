try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a number")
else:
    print("Square:", number * number)
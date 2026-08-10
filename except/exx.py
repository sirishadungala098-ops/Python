try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    result=num1/num2
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Result:", result)
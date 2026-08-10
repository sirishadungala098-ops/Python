try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1/num2
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Division result",result)
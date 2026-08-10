try:
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
except ZeroDivisionError:
    print("division by zero is error")
else:
    print("division:",x/y)
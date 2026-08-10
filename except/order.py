try:
    num=int(input("Enter a number:"))
    print(100/num)
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("Cannot be divide by zero")
except Ecxeption as error:
    print("Unexpected error",error)
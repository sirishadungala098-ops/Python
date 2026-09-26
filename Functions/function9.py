def iseven(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
num=int(input("Enter a number: "))
print(iseven(num))
def ispositive(a):
    if a > 0:
        return "Positive"
    elif a < 0:
        return "Negative"
    else:
        return "Zero"
num=int(input("Enter a number: "))
print(ispositive(num))
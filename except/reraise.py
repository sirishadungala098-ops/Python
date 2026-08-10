try:
    num=int(input("Enter a number:"))
    if num<0:
        raise ValueError("negative values are not allowed")
except ValueError as error:
    print("Error detected",error)
    raise
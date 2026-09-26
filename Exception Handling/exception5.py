try:
    text = "hello"
    number = int(text)
    print(number)
except ValueError:
    print("Cannot convert string into integer")
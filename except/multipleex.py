try: 
    number = int(input("Enter a number:")) 
    result = 100 / number 
    print(result) 
except (ValueError, ZeroDivisionError):
    print("Invalid division by zero occurred")
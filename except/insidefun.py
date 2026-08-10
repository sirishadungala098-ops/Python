def divide_numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return "cannot be divide by zero"
print(divide_numbers(20,4))
print(divide_numbers(20,0))
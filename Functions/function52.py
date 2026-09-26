def tuple_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
numbers = (10, 20, 30, 40)
print("Sum:", tuple_sum(numbers))
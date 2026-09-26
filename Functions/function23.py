def average(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total / len(numbers)
print(average([10, 20, 30, 40, 50]))
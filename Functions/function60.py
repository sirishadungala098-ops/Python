def number_squares(numbers):
    result = {}
    for num in numbers:
        result[num] = num * num
    return result
numbers = [2, 4, 6, 8]
print(number_squares(numbers))
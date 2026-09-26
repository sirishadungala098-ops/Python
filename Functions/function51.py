def min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return (minimum, maximum)
numbers = [10, 25, 5, 40, 15]
print(min_max(numbers))
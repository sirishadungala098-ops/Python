def largest(numbers):
    large = numbers[0]
    for i in numbers:
        if i > large:
            large = i
    return large
numbers = [10, 20, 30, 15]
print(largest(numbers))
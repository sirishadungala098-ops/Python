def largest_smallest(numbers):
    large = numbers[0]
    small = numbers[0]
    for i in numbers:
        if i > large:
            large = i
        if i < small:
            small = i
    return large, small
print(largest_smallest([10, 5, 20, 3, 15]))
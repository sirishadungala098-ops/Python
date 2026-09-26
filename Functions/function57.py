def count_even_odd(numbers):
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return {
        "Even": even,
        "Odd": odd
    }
numbers = [10, 15, 20, 25, 30, 35]
print(count_even_odd(numbers))
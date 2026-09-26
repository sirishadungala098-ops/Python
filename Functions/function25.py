def odd(numbers):
    result = []
    for i in numbers:
        if i % 2 != 0:
            result.append(i)
    return result
print(odd([1, 2, 3, 4, 5, 6]))
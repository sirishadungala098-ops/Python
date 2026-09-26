def remove_duplicates(numbers):
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicates([1, 2, 2, 3, 3, 4]))
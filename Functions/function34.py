def calculate_sum(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(calculate_sum(10, 20, 30))
print(calculate_sum(5, 10, 15, 20, 25))
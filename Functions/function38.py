def average(*args):
    total = 0
    for num in args:
        total = total + num
    avg = total / len(args)
    return avg
print("Average:", average(10, 20, 30, 40, 50))
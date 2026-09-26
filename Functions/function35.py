def largest(*args):
    large = args[0]
    for num in args:
        if num > large:
            large = num
    return large
print("Largest:", largest(10, 50, 25, 80, 35))
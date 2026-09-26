def even_odd(*args):
    even = []
    odd = []
    for num in args:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print("Even numbers:", even)
    print("Odd numbers:", odd)
even_odd(10, 15, 20, 25, 30, 35, 40)
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
with open("even.txt", "w") as even_file:
    with open("odd.txt", "w") as odd_file:
        for line in numbers:
            num = int(line)
            if num % 2 == 0:
                even_file.write(str(num) + "\n")
            else:
                odd_file.write(str(num) + "\n")
print("Even and odd numbers separated")
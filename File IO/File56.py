with open("numbers.txt", "r") as file:
    numbers = file.readlines()
with open("squares.txt", "w") as file:
    for line in numbers:
        num = int(line)
        file.write(str(num * num) + "\n")
print("Squares created")
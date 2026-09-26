with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]
numbers.sort()
with open("sorted.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")
print("Numbers sorted successfully")
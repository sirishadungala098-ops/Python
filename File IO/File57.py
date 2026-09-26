with open("numbers.txt", "r") as file:
    numbers = file.readlines()
with open("cubes.txt", "w") as file:
    for line in numbers:
        num = int(line)
        file.write(str(num * num * num) + "\n")
print("Cubes created")
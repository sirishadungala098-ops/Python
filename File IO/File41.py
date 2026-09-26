with open("numbers.txt", "r") as file:
    numbers = file.readlines()
with open("even.txt", "w") as file:
    for num in numbers:
        if int(num) % 2 == 0:
            file.write(num)
print("Even numbers written successfully")
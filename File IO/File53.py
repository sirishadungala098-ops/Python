with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)
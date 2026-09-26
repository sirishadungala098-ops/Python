with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate numbers:", duplicates)
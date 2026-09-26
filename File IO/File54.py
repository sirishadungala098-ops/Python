with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)
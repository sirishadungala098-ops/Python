total = 0
count = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
        count += 1
average = total / count
print("Average:", average)
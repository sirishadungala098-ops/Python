with open("numbers.txt", "w") as file:
    for i in range(1, 21):
        file.write(str(i) + "\n")
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print("Total:", total)
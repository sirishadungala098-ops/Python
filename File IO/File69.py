total = 0
count = 0
with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        total += int(data[4])
        count += 1
average = total / count
print("Average marks:", average)
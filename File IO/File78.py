import csv
total = 0
count = 0
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += int(row["Marks"])
        count += 1
average = total / count
print("Average marks:", average)
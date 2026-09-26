import csv
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([104, "Sita", "HTML", 88])
print("New student added")
import csv
with open("students.csv", "r") as file:
    rows = list(csv.DictReader(file))
rows.sort(key=lambda row: int(row["Marks"]))
with open("sorted_students.csv", "w", newline="") as file:
    fieldnames = ["ID", "Name", "Course", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print("Students sorted successfully")
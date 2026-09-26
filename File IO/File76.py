import csv
student_id = input("Enter student ID: ")
with open("students.csv", "r") as file:
    rows = list(csv.DictReader(file))
new_rows = []
for row in rows:
    if row["ID"] != student_id:
        new_rows.append(row)
with open("students.csv", "w", newline="") as file:
    fieldnames = ["ID", "Name", "Course", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)
print("Student deleted")
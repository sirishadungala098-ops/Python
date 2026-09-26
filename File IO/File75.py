import csv
student_id = input("Enter student ID: ")
new_marks = input("Enter new marks: ")
with open("students.csv", "r") as file:
    rows = list(csv.DictReader(file))
for row in rows:
    if row["ID"] == student_id:
        row["Marks"] = new_marks
with open("students.csv", "w", newline="") as file:
    fieldnames = ["ID", "Name", "Course", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print("Marks updated")
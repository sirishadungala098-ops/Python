import json
student_id = int(input("Enter student ID: "))
with open("students.json", "r") as file:
    students = json.load(file)
for student in students:
    if student["id"] == student_id:
        student["marks"] = 95
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print("Student information updated")
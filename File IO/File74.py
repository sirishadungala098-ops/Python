import csv
student_id = input("Enter student ID: ")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["ID"] == student_id:
            print(row)
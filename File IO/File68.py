student_id = input("Enter student ID: ")
with open("students.txt", "r") as file:
    lines = file.readlines()
with open("students.txt", "w") as file:
    for line in lines:
        data = line.strip().split(",")
        if data[0] != student_id:
            file.write(line)
print("Student record deleted")
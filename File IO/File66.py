student_id = input("Enter student ID: ")
new_marks = input("Enter new marks: ")
with open("students.txt", "r") as file:
    lines = file.readlines()
with open("students.txt", "w") as file:
    for line in lines:
        data = line.strip().split(",")

        if data[0] == student_id:
            data[4] = new_marks
            file.write(",".join(data) + "\n")
        else:
            file.write(line)
print("Marks updated")
with open("students.txt", "r") as file:
    lines = file.readlines()
highest = 0
student = ""
for line in lines:
    data = line.strip().split(",")
    marks = int(data[4])
    if marks > highest:
        highest = marks
        student = line.strip()
print("Highest marks:", highest)
print("Student:", student)
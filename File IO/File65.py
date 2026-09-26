student_id = input("Enter student ID: ")
with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[0] == student_id:
            print("Student found:", line.strip())
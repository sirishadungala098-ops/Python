name = input("Enter student name: ")
with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        if data[1].lower() == name.lower():
            print("Student found:", line.strip())
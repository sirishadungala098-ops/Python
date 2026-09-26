with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        marks = int(data[4])
        if marks > 75:
            print(line.strip())
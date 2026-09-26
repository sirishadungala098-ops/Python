import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Course", "Marks"])
    writer.writerow([101, "John", "Python", 85])
    writer.writerow([102, "Aishu", "Java", 78])
    writer.writerow([103, "Ravi", "Python", 92])
print("CSV file created")
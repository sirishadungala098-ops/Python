students=[("Sirisha","CCN",21),("Sravya","CCN",22),("Tanuu","CCN",2),("Januu","CCN",12)]
name=input("Enter student name:")
found=False
for student in students:
    if student[0]==name:
        print("Found student",student)
        found=True
        break
else:
    print("Not found")
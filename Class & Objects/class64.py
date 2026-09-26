class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
s1 = Student("Sirisha")
s2 = Student("Janu")
s3 = Student("Sri")
print("Total students:", Student.count)
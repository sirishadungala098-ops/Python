class Student:
    college_name = "Aditya College"
    def __init__(self, name):
        self.name = name
s1 = Student("Sirisha")
s2 = Student("Sri")
print(s1.name, s1.college_name)
print(s2.name, s2.college_name)
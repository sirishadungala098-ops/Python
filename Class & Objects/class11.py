class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
s1 = Student("Sirisha", 20, "Python")
s2 = Student("Sri", 21, "Java")
s3 = Student("Janu", 19, "HTML")
print(s1.name, s1.age, s1.course)
print(s2.name, s2.age, s2.course)
print(s3.name, s3.age, s3.course)
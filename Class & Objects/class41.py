class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
s = Student("Sirisha", 20, "Python", 85)
print(s.name)
print(s.age)
print(s.course)
print(s.marks)
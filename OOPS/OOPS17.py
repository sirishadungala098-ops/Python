class Teacher:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Teacher:", self.name)
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Student:", self.name)
class School:
    def __init__(self):
        self.teacher = Teacher("Priya")
        self.student = Student("Ravi")
    def display(self):
        self.teacher.display()
        self.student.display()
school = School()
school.display()
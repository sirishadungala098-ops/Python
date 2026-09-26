class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Student:", self.name)
class College:
    def __init__(self):
        self.students = [
            Student("Ravi"),
            Student("Priya"),
            Student("Sirisha")
        ]
    def display_students(self):
        for student in self.students:
            student.display()
college = College()
college.display_students()
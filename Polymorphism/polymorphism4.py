class Student:
    def display(self):
        print("Student: Sirisha")
class Teacher:
    def display(self):
        print("Teacher: Python Teacher")
people = [Student(), Teacher()]
for person in people:
    person.display()
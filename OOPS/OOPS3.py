class Person:
    def show_name(self):
        print("Name: Sirisha")
class Student(Person):
    def study(self):
        print("Student is studying")
student = Student()
student.show_name()
student.study()
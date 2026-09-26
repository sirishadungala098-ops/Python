class Course:
    def study(self):
        print("Student is studying Python")
class Person:
    def introduce(self):
        print("I am a person")
class Student(Person):
    def __init__(self):
        self.course = Course()
    def study_course(self):
        self.course.study()
student = Student()
student.introduce()
student.study_course()
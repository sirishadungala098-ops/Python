class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
    def enroll(self, student):
        self.students.append(student)
    def display_students(self):
        print("Course:", self.course_name)
        for student in self.students:
            print(student)
c = Course("Python")
c.enroll("Sirisha")
c.enroll("Janu")
c.enroll("Sri")
c.display_students()
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def study(self):
        print(self.name, "is studying")
class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")
class NotificationService:
    def send(self, message):
        print("Notification:", message)
class CertificateGenerator:
    def generate(self, student):
        print("Certificate generated for", student)
class Course:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students
    def complete(self, notification, certificate):
        notification.send(self.name + " course completed")
        for student in self.students:
            certificate.generate(student.name)
teacher = Teacher("Priya")
students = [
    Student("Sirisha"),
    Student("Ravi")
]
course = Course("Python", teacher, students)
notification = NotificationService()
certificate = CertificateGenerator()
teacher.teach()
students[0].study()
course.complete(notification, certificate)
class Teacher:
    def __init__(self, name):
        self.name = name
class Student:
    def __init__(self, name):
        self.name = name
class NotificationService:
    def send(self, message):
        print("Notification:", message)
class School:
    def __init__(self):
        self.teachers = [
            Teacher("Priya"),
            Teacher("Ravi")
        ]
        self.students = [
            Student("Arun"),
            Student("Sita")
        ]
    def send_notification(self, service):
        service.send("School will be closed tomorrow")
school = School()
notification = NotificationService()
school.send_notification(notification)
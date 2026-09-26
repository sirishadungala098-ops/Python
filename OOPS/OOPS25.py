class NotificationService:
    def send(self, message):
        print("Notification:", message)
class Student:
    def __init__(self, name):
        self.name = name
    def send_notification(self, service):
        service.send("Hello " + self.name)
student = Student("Sirisha")
service = NotificationService()
student.send_notification(service)
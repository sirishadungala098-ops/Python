from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class Email(Notification):
    def send(self):
        print("Sending Email")
class SMS(Notification):
    def send(self):
        print("Sending SMS")
class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp message")
notifications = [Email(), SMS(), WhatsApp()]
for notification in notifications:
    notification.send()
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def schedule(self):
        pass
class Email(Notification):
    def send(self):
        print("Email sent")

    def schedule(self):
        print("Email scheduled")
class SMS(Notification):
    def send(self):
        print("SMS sent")
    def schedule(self):
        print("SMS scheduled")
class WhatsApp(Notification):
    def send(self):
        print("WhatsApp message sent")
    def schedule(self):
        print("WhatsApp message scheduled")
email = Email()
sms = SMS()
whatsapp = WhatsApp()

email.send()
email.schedule()

sms.send()
sms.schedule()

whatsapp.send()
whatsapp.schedule()
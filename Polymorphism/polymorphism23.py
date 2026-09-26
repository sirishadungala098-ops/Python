class Email:
    def send(self):
        print("Sending Email")
class SMS:
    def send(self):
        print("Sending SMS")
class WhatsApp:
    def send(self):
        print("Sending WhatsApp")
def send_notification(notification):
    notification.send()
send_notification(Email())
send_notification(SMS())
send_notification(WhatsApp())
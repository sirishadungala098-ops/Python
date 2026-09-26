class EmailNotification:
    def send(self):
        print("Sending Email")
class SMSNotification:
    def send(self):
        print("Sending SMS")
notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()
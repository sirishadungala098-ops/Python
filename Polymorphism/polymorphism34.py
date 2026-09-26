class EmailService:
    def send(self):
        print("Sending Email")
class SMSService:
    def send(self):
        print("Sending SMS")
def send_message(service):
    service.send()
send_message(EmailService())
send_message(SMSService())
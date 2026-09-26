class EmailService:
    def send_email(self, message):
        print("Email sent:", message)
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
    def send_confirmation(self, email_service):
        email_service.send_email(
            "Order " + str(self.order_id) + " confirmed"
        )
order = Order(101)
email = EmailService()
order.send_confirmation(email)
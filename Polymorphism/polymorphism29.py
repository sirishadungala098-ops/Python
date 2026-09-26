class AmazonDelivery:
    def deliver(self):
        print("Amazon delivery completed")
class FlipkartDelivery:
    def deliver(self):
        print("Flipkart delivery completed")
class CourierDelivery:
    def deliver(self):
        print("Courier delivery completed")
def process_delivery(delivery):
    delivery.deliver()
process_delivery(AmazonDelivery())
process_delivery(FlipkartDelivery())
process_delivery(CourierDelivery())
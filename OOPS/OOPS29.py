class DeliveryService:
    def deliver(self, food):
        print(food, "is delivered")
class FoodOrder:
    def __init__(self, food):
        self.food = food
    def send_for_delivery(self, delivery_service):
        delivery_service.deliver(self.food)
order = FoodOrder("Pizza")
delivery = DeliveryService()
order.send_for_delivery(delivery)
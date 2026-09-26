from abc import ABC, abstractmethod
class Delivery(ABC):
    @abstractmethod
    def calculate_delivery_charge(self):
        pass
class StandardDelivery(Delivery):
    def calculate_delivery_charge(self):
        print("Standard delivery charge: 50")
class ExpressDelivery(Delivery):
    def calculate_delivery_charge(self):
        print("Express delivery charge: 100")
class SameDayDelivery(Delivery):
    def calculate_delivery_charge(self):
        print("Same-day delivery charge: 150")
deliveries = [
    StandardDelivery(),
    ExpressDelivery(),
    SameDayDelivery()
]
for delivery in deliveries:
    delivery.calculate_delivery_charge()
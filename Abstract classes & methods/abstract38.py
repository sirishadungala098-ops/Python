from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def charge(self):
        pass

class StandardDelivery(Delivery):
    def charge(self):
        print("Standard charge: 50")

class ExpressDelivery(Delivery):
    def charge(self):
        print("Express charge: 100")

deliveries = [StandardDelivery(), ExpressDelivery()]

for delivery in deliveries:
    delivery.charge()
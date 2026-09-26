from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class StandardDelivery(Delivery):
    def calculate_charge(self):
        print("Standard delivery charge:50")

    def deliver(self):
        print("Product delivered by standard delivery")
class ExpressDelivery(Delivery):
    def calculate_charge(self):
        print("Express delivery charge:100")
    def deliver(self):
        print("Product delivered by express delivery")
standard = StandardDelivery()
express = ExpressDelivery()

standard.calculate_charge()
standard.deliver()

express.calculate_charge()
express.deliver()
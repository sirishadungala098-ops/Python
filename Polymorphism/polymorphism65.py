class Car:
    def start(self):
        print("Car starts with key")
class Bike:
    def start(self):
        print("Bike starts with self-start")
class Bus:
    def start(self):
        print("Bus starts with engine")
class Truck:
    def start(self):
        print("Truck starts with engine")
vehicles = [Car(), Bike(), Bus(), Truck()]
for vehicle in vehicles:
    vehicle.start()
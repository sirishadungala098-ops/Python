class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")
class Bus(Vehicle):
    def start(self):
        print("Bus starts with engine")
vehicles = [Car(), Bike(), Bus()]
for vehicle in vehicles:
    vehicle.start()
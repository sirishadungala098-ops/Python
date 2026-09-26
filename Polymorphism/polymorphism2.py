class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
class Bus:
    def start(self):
        print("Bus starts")
vehicles = [Car(), Bike(), Bus()]
for vehicle in vehicles:
    vehicle.start()
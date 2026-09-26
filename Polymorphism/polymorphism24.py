class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
class Bus:
    def start(self):
        print("Bus starts")
def start_vehicle(vehicle):
    vehicle.start()
start_vehicle(Car())
start_vehicle(Bike())
start_vehicle(Bus())
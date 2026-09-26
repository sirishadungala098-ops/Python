class Car:
    def start(self):
        print("Car starts")
class Bike:
    def start(self):
        print("Bike starts")
def start_vehicle(vehicle):
    vehicle.start()
start_vehicle(Car())
start_vehicle(Bike())
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
car = Car()
car.start()
car.drive()
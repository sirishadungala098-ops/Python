class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
    def display(self):
        print("Brand:", self.brand)
c = Car("BMW")
c.start()
c.display()
c.stop()
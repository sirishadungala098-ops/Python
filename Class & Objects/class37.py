class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def display_details(self):
        print("Brand:", self.brand)
c = Car("BMW")
c.start()
c.display_details()
c.stop()
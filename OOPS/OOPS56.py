class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
class Customer:
    def __init__(self, name):
        self.name = name
class PaymentService:
    def pay(self, amount):
        print("Rental payment:", amount)
class Rental:
    def __init__(self, customer, vehicle):
        self.customer = customer
        self.vehicle = vehicle
    def rent_vehicle(self, payment):
        print(self.customer.name, "rented", self.vehicle.name)
        payment.pay(self.vehicle.price)
customer = Customer("Sirisha")
car = Car("Car", 2000)
rental = Rental(customer, car)
payment = PaymentService()
rental.rent_vehicle(payment)
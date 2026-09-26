class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
c1 = Car("Toyota", "Innova", 2023, 2500000)
c2 = Car("BMW", "X5", 2024, 7000000)
c3 = Car("Audi", "A4", 2022, 5000000)
print(c1.brand, c1.model, c1.year, c1.price)
print(c2.brand, c2.model, c2.year, c2.price)
print(c3.brand, c3.model, c3.year, c3.price)
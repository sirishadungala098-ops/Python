from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

class Product1(Product):
    def calculate_discount(self):
        print("Discount:", self.price * 10 / 100)

p = Product1("Mobile", 20000)
p.calculate_discount()
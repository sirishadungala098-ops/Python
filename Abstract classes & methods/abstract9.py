from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass
class Pizza(Food):
    def prepare(self):
        print("Pizza is prepared with cheese and toppings")
class Burger(Food):
    def prepare(self):
        print("Burger is prepared with bread and vegetables")
pizza = Pizza()
burger = Burger()
pizza.prepare()
burger.prepare()
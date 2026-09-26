from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Color:", self.color)
        print("Area:", 78.5)

c = Circle("Red")
c.area()
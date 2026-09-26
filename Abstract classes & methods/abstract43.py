from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def display_shape(self):
        print("Shape: Circle")


class Circle(Shape):

    def area(self):
        print("Area:", 3.14 * 5 * 5)


c = Circle()
c.area()
c.display_shape()
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        radius = 5
        print("Circle area:", 3.14 * radius * radius)
class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Rectangle area:", length * width)
circle = Circle()
rectangle = Rectangle()

circle.area()
rectangle.area()
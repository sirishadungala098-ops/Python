from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area of rectangle:", 10 * 5)
    def perimeter(self):
        print("Perimeter of rectangle:", 2 * (10 + 5))
class Circle(Shape):
    def area(self):
        print("Area of circle:", 3.14 * 5 * 5)
    def perimeter(self):
        print("Perimeter of circle:", 2 * 3.14 * 5)
rectangle = Rectangle()
circle = Circle()
rectangle.area()
rectangle.perimeter()
circle.area()
circle.perimeter()
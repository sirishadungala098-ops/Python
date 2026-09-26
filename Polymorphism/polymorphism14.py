class Shape:
    def area(self):
        print("Shape area")
class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Rectangle area:", length * width)
class Circle(Shape):
    def area(self):
        radius = 5
        print("Circle area:", 3.14 * radius * radius)
class Triangle(Shape):
    def area(self):
        base = 10
        height = 6
        print("Triangle area:", 0.5 * base * height)
shapes = [Rectangle(), Circle(), Triangle()]
for shape in shapes:
    shape.area()
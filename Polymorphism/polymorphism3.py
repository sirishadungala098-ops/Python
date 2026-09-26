class Rectangle:
    def area(self):
        length = 10
        width = 5
        print("Rectangle area:", length * width)
class Circle:
    def area(self):
        radius = 5
        print("Circle area:", 3.14 * radius * radius)
shapes = [Rectangle(), Circle()]
for shape in shapes:
    shape.area()
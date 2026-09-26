class Shape:
    def display(self):
        print("This is a shape")
class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Area:", length * width)
rectangle = Rectangle()
rectangle.display()
rectangle.area()
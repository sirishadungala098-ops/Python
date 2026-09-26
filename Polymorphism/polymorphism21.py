class Rectangle:
    def area(self):
        print("Rectangle area:", 10 * 5)
class Circle:
    def area(self):
        print("Circle area:", 3.14 * 5 * 5)
def calculate_area(shape):
    shape.area()
calculate_area(Rectangle())
calculate_area(Circle())
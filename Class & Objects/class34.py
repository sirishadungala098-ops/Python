class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
    def perimeter(self):
        print(2 * (self.length + self.width))
r = Rectangle(10, 5)
r.area()
r.perimeter()
import math
class Circle:
    def calculate_area(self):
        r = 5
        return math.pi * r * r
class Rectangle:
    def calculate_area(self):
        length = 10
        width = 5
        return length * width
class Square:
    def calculate_area(self):
        side = 6
        return side * side
class Triangle:
    def calculate_area(self):
        base = 10
        height = 5
        return 0.5 * base * height
shapes = [Circle(), Rectangle(), Square(), Triangle()]
for shape in shapes:
    print("Area:", shape.calculate_area())
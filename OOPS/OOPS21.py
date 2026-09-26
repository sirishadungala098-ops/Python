class Printer:
    def print_details(self, details):
        print(details)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_details(self, printer):
        details = "Name: " + self.name + ", Marks: " + str(self.marks)
        printer.print_details(details)
student = Student("Sirisha", 90)
printer = Printer()
student.show_details(printer)
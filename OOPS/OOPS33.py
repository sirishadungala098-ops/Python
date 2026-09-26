class Printer:
    def print_data(self, data):
        print("Printing:", data)
class Student:
    def print_details(self, printer):
        printer.print_data("Student Details")
student = Student()
printer = Printer()
student.print_details(printer)
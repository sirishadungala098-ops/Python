class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_salary(self):
        print(self.name)
        print(self.salary)
e1 = Employee("Ravi", 30000)
e1.display_salary()
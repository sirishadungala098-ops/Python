from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print(self.name, "Salary: 50000")

m = Manager("Ravi", 101)
m.calculate_salary()
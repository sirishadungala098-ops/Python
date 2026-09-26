from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary:80000")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary:60000")
class Tester(Employee):
    def calculate_salary(self):
        print("Tester salary: 50000")
employees = [Manager(), Developer(), Tester()]
for employee in employees:
    employee.calculate_salary()
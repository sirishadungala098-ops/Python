from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print("Manager salary: 50000")

class Developer(Employee):
    def salary(self):
        print("Developer salary: 40000")

employees = [Manager(), Developer()]

for employee in employees:
    employee.salary()
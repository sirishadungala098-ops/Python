from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass
class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary: 60000")
    def display_details(self):
        print("Manager: Ravi")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 50000")
    def display_details(self):
        print("Developer: Sirisha")
manager = Manager()
developer = Developer()

manager.display_details()
manager.calculate_salary()

developer.display_details()
developer.calculate_salary()
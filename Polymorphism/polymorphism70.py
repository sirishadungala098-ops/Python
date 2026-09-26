from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def work(self):
        pass
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
    def __add__(self, other):
        return self.salary + other.salary
class Developer(Employee):
    def work(self):
        print(self.name, "writes code")
class Tester(Employee):
    def work(self):
        print(self.name, "tests software")
class Manager(Employee):
    def work(self):
        print(self.name, "manages the team")
developer = Developer("Ravi", 50000)
tester = Tester("Priya", 40000)
manager = Manager("Arun", 60000)
developer.work()
tester.work()
manager.work()
developer.display()
total_salary = developer + tester
print("Total Salary:", total_salary)
class Freelancer:
    def work(self):
        print("Freelancer works on projects")
class Student:
    def work(self):
        print("Student works on assignments")
def start_work(obj):
    obj.work()
freelancer = Freelancer()
student = Student()
start_work(freelancer)
start_work(student)
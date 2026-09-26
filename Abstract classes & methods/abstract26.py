from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

class Manager(Employee):
    def work(self):
        print("Manager works")

class Developer(Employee):
    def work(self):
        print("Developer codes")

class Tester(Employee):
    def work(self):
        print("Tester tests")

Manager("Raghu", 50000).work()
Developer("Sirisha", 40000).work()
Tester("Janu", 30000).work()
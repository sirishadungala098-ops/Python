from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("Developer writes code")
class Tester(Employee):
    def work(self):
        print("Tester tests the application")
developer = Developer()
tester = Tester()
developer.work()
tester.work()
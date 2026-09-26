class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def code(self):
        print("Developer writes code")
class Tester(Employee):
    def test(self):
        print("Tester tests software")
class Manager(Employee):
    def manage(self):
        print("Manager manages the team")
developer = Developer()
tester = Tester()
manager = Manager()
developer.work()
developer.code()
tester.work()
tester.test()
manager.work()
manager.manage()
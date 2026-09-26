class Laptop:
    def use(self):
        print("Developer is using laptop")
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def __init__(self):
        self.laptop = Laptop()
    def code(self):
        self.laptop.use()
        print("Developer is writing code")
developer = Developer()
developer.work()
developer.code()
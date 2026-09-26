class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Developer(Employee):
    def work(self):
        print(self.name, "writes code")
class Manager(Employee):
    def work(self):
        print(self.name, "manages team")
class Department:
    def __init__(self, name):
        self.name = name
class PaymentService:
    def pay(self, name, salary):
        print("Paid", salary, "to", name)
class PayrollService:
    def process(self, employee, payment):
        payment.pay(employee.name, employee.salary)
class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR")
        ]
        self.employees = [
            Developer("Ravi", 50000),
            Manager("Priya", 70000)
        ]
company = Company()
payment = PaymentService()
payroll = PayrollService()
company.employees[0].work()
payroll.process(company.employees[0], payment)
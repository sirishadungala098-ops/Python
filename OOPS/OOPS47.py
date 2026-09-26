class Department:
    def __init__(self, name):
        self.name = name
class Employee:
    def __init__(self, name):
        self.name = name
class PayrollService:
    def process_salary(self):
        print("Employee salaries processed")
class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR")
        ]
        self.employees = [
            Employee("Ravi"),
            Employee("Priya")
        ]
    def process_payroll(self, payroll):
        payroll.process_salary()
company = Company()
payroll = PayrollService()
company.process_payroll(payroll)
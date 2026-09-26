class Employee:
    def __init__(self, salary):
        self.salary = salary
    def annual_salary(self):
        print("Annual Salary:", self.salary * 12)
e = Employee(30000)
e.annual_salary()
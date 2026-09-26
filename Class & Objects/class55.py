class Employee:
    def __init__(self, daily_salary):
        self.daily_salary = daily_salary
    def salary(self, days):
        return self.daily_salary * days
e = Employee(1000)
print(e.salary(20))
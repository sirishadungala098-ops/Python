class Manager:
    def calculate_salary(self):
        return 80000
class Developer:
    def calculate_salary(self):
        return 60000
class Tester:
    def calculate_salary(self):
        return 45000
class Intern:
    def calculate_salary(self):
        return 20000
employees = [Manager(), Developer(), Tester(), Intern()]
for employee in employees:
    print("Salary:", employee.calculate_salary())
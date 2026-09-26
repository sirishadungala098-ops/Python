class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
e1 = Employee("Siri", "HR", 30000)
e2 = Employee("Tanuu", "IT", 40000)
e3 = Employee("Janu", "Sales", 35000)
e4 = Employee("Divya", "Finance", 45000)
e5 = Employee("Esha", "IT", 50000)
print(e1.name, e1.department, e1.salary)
print(e2.name, e2.department, e2.salary)
print(e3.name, e3.department, e3.salary)
print(e4.name, e4.department, e4.salary)
print(e5.name, e5.department, e5.salary)
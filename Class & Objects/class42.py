class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
e = Employee(101, "Ravi", "IT", 30000)
print(e.id)
print(e.name)
print(e.department)
print(e.salary)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __gt__(self, other):
        return self.salary > other.salary
e1 = Employee("Raghu", 60000)
e2 = Employee("Sagar", 50000)
print(e1 > e2)
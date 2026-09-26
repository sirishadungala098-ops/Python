class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, name):
        self.employees.append(name)
    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print(name, "removed")
    def search_employee(self, name):
        if name in self.employees:
            print(name, "found")
        else:
            print(name, "not found")
    def display_employees(self):
        print("Employees:")
        for employee in self.employees:
            print(employee)
company = Company()
company.add_employee("Sirisha")
company.add_employee("Janu")
company.add_employee("Raghu")
company.display_employees()
company.search_employee("Janu")
company.remove_employee("Raghu")
company.display_employees()
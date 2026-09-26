from abc import ABC, abstractmethod

class EmployeePayroll(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Full-time salary: ₹50,000")


class PartTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Part-time salary: ₹20,000")


class ContractEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Contract salary: ₹30,000")


FullTimeEmployee().calculate_salary()
PartTimeEmployee().calculate_salary()
ContractEmployee().calculate_salary()
class SalesReport:
    def generate(self):
        print("Generating Sales Report")
class StudentReport:
    def generate(self):
        print("Generating Student Report")
class EmployeeReport:
    def generate(self):
        print("Generating Employee Report")
def generate_report(report):
    report.generate()
generate_report(SalesReport())
generate_report(StudentReport())
generate_report(EmployeeReport())
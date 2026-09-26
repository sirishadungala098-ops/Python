class ReportGenerator:
    def generate(self, name):
        print("Report generated for", name)
class Employee:
    def __init__(self, name):
        self.name = name
    def create_report(self, report_generator):
        report_generator.generate(self.name)
employee = Employee("Ravi")
report = ReportGenerator()
employee.create_report(report)
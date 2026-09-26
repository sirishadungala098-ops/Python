class ExcelReport:
    def generate(self):
        print("Generating Excel Report")
class PDFReport:
    def generate(self):
        print("Generating PDF Report")
def generate_report(report):
    report.generate()
generate_report(ExcelReport())
generate_report(PDFReport())
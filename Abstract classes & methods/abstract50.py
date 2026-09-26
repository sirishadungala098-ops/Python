from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        print("Report: Student Report")


class PDFReport(Report):

    def generate(self):
        print("PDF report generated")


r = PDFReport()
r.generate()
r.display_report_info()
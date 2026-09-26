class Printer:
    def print(self):
        print("Printing document")
class PDFPrinter:
    def print(self):
        print("Printing PDF document")
def print_document(printer):
    printer.print()
print_document(Printer())
print_document(PDFPrinter())
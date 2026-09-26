from abc import ABC, abstractmethod
class Tax(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass
class IncomeTax(Tax):
    def calculate_tax(self):
        print("Income tax calculated")
class GST(Tax):
    def calculate_tax(self):
        print("GST calculated")
class PropertyTax(Tax):
    def calculate_tax(self):
        print("Property tax calculated")
taxes = [IncomeTax(), GST(), PropertyTax()]
for tax in taxes:
    tax.calculate_tax()
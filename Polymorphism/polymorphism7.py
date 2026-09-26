class PDF:
    def open(self):
        print("Opening PDF file")
class Word:
    def open(self):
        print("Opening Word file")
class Excel:
    def open(self):
        print("Opening Excel file")
files = [PDF(), Word(), Excel()]
for file in files:
    file.open()
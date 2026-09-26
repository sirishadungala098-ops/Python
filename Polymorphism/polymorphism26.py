class PDF:
    def read(self):
        print("Reading PDF file")
class Word:
    def read(self):
        print("Reading Word file")
class Excel:
    def read(self):
        print("Reading Excel file")
def read_file(file):
    file.read()
read_file(PDF())
read_file(Word())
read_file(Excel())
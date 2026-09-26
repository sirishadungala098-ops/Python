from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

class PDFFile(FileHandler):
    def read(self):
        print("Reading PDF")

class CSVFile(FileHandler):
    def read(self):
        print("Reading CSV")

files = [PDFFile(), CSVFile()]

for file in files:
    file.read()
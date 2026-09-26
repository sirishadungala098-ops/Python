class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __gt__(self, other):
        return self.marks > other.marks
student1 = Student("Sirisha", 85)
student2 = Student("Janu", 75)
print(student1 > student2)
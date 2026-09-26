class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 50:
            print("Grade C")
        else:
            print("Fail")
s = Student("Sirisha", 85)
s.grade()
class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def total(self):
        print("Total:", self.m1 + self.m2 + self.m3)
    def average(self):
        print("Average:", (self.m1 + self.m2 + self.m3) / 3)
s = Student(80, 90, 70)
s.total()
s.average()
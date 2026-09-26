class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self, student):
        return student.name + " " + str(student.age)
s1 = Student("Sirisha", 21)
s2 = Student("Janu", 22)
print(s1.get_info(s2))
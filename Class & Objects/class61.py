class Student:
    college = "Aditya College"  
    def __init__(self, name):
        self.name = name      
s1 = Student("Sirisha")
s2 = Student("Janu")
print(s1.name)
print(s2.name)
print(s1.college)
print(s2.college)
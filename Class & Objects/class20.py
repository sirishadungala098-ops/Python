class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
t1 = Teacher("Ravi", "Python", 5)
t2 = Teacher("Anu", "Java", 3)
t3 = Teacher("Kiran", "SQL", 7)
print(t1.name, t1.subject, t1.experience)
print(t2.name, t2.subject, t2.experience)
print(t3.name, t3.subject, t3.experience)
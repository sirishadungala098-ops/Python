from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        print("Student")

class Teacher(Person):
    def role(self):
        print("Teacher")

class Doctor(Person):
    def role(self):
        print("Doctor")

Student("Sirisha", 21).role()
Teacher("Raghu", 35).role()
Doctor("Anil", 40).role()
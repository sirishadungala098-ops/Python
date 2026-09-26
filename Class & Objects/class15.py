class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
p1 = Person("Sirisha", 20, "Hyderabad")
p2 = Person("Sri", 21, "Chennai")
print(p1.name, p1.age, p1.city)
print(p2.name, p2.age, p2.city)
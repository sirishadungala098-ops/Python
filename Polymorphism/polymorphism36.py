class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
class Cow:
    def sound(self):
        print("Cow moos")
def make_sound(animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())
make_sound(Cow())
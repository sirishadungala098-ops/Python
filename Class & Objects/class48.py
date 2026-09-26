class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating
    def display(self):
        print(self.name)
        print(self.hero)
        print(self.heroine)
        print(self.rating)
m = Movie("Darling", "Prabhas", "Kajal", 9)
m.display()
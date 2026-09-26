class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating
m1 = Movie("RRR", "NTR", "Alia", 9)
m2 = Movie("Bahubali", "Prabhas", "Anushka", 9.5)
print(m1.name, m1.hero, m1.heroine, m1.rating)
print(m2.name, m2.hero, m2.heroine, m2.rating)
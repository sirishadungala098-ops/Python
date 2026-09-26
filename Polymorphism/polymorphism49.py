class Temperature:
    def __init__(self, value):
        self.value = value
    def __gt__(self, other):
        return self.value > other.value
t1 = Temperature(35)
t2 = Temperature(30)
print(t1 > t2)
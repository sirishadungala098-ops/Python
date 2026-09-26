class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
m1 = Mobile("Samsung", "S25", 50000)
print(m1.brand)
print(m1.model)
print(m1.price)
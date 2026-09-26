class Pizza:
    def calculate_price(self):
        return 300
class Burger:
    def calculate_price(self):
        return 150
class Biryani:
    def calculate_price(self):
        return 250
class IceCream:
    def calculate_price(self):
        return 100
foods = [Pizza(), Burger(), Biryani(), IceCream()]
total = 0
for food in foods:
    price = food.calculate_price()
    print("Price:", price)
    total = total + price
print("Total Price:", total)
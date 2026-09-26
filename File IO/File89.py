import json
total = 0
with open("products.json", "r") as file:
    products = json.load(file)
for product in products:
    value = product["price"] * product["quantity"]
    total += value
print("Total inventory value:", total)
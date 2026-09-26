import json
products = [
    {
        "name": "Laptop",
        "price": 50000,
        "quantity": 2
    },
    {
        "name": "Mouse",
        "price": 500,
        "quantity": 5
    },
    {
        "name": "Keyboard",
        "price": 1000,
        "quantity": 3
    }
]
with open("products.json", "w") as file:
    json.dump(products, file, indent=4)
print("Product JSON file created")
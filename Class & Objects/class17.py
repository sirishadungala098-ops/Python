class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price
l1 = Laptop("Dell", "8GB", "512GB", 50000)
l2 = Laptop("HP", "16GB", "1TB", 70000)
l3 = Laptop("Lenovo", "8GB", "512GB", 45000)
print(l1.brand, l1.ram, l1.storage, l1.price)
print(l2.brand, l2.ram, l2.storage, l2.price)
print(l3.brand, l3.ram, l3.storage, l3.price)
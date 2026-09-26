products={
    "Laptop":15000,
    "Watch":1000,
    "Computer":25000,
    "Smart phone":30000,
    "Keyboard":1500
}
for product,price in products.items():
    if price>1000:
        print(product,":",price)
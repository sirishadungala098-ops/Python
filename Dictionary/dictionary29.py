products={
    "laptop":75000,
    "computer":50000,
    "keyboard":4500,
    "mouse":5500,
    "watch":6000
}
for product,price in products.items():
    if price>5000:
        print(product,price)
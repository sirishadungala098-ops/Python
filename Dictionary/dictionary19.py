products={
    "pen":10,
    "pencil":8,
    "Sketches":6,
    "Laptop":12,
    "Computer":15
}
for product,quantity in products.items():
    if quantity < 10:
        print(product,quantity)
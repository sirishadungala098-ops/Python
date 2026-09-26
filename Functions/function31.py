def total_price(price, tax=18):
    tax_amount = price * tax / 100
    total = price + tax_amount
    return total
print(total_price(1000))
print(total_price(1000, 10))
try:
    l1=[10,20,30,40]
    print(l1)
    print(l1[6])
except IndexError:
    print("specified index does not exist")
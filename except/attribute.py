try:
    num=100
    num.append(20)
except AttributeError:
    print("Integer objects do not have an append method")
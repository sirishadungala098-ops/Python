try:
    with open("sample.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Permission denied")
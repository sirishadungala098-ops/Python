filename = input("Enter filename: ")
try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist")
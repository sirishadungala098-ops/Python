file = None
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
        print("File closed")
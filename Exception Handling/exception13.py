try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content)
finally:
    print("File operation completed")
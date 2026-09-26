with open("sample.txt", "r") as file:
    content = file.read()
with open("lowercase.txt", "w") as file:
    file.write(content.lower())
print("Text converted to lowercase")
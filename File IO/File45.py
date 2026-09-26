with open("sample.txt", "r") as file:
    content = file.read()
content = " ".join(content.split())
with open("new.txt", "w") as file:
    file.write(content)
print("Extra spaces removed")
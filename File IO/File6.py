file = open("sample.txt", "r")
content = file.read()
for character in content:
    print(character)
file.close()
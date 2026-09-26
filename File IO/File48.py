with open("sample.txt", "r") as file:
    lines = file.readlines()
with open("reverse_lines.txt", "w") as file:
    for line in lines:
        file.write(line.rstrip("\n")[::-1] + "\n")
print("Lines reversed successfully")
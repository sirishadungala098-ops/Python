with open("sample.txt", "r") as file:
    content = file.read()
count = 0
for ch in content:
    if ch == " ":
        count += 1
print("Total spaces:", count)
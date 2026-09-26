with open("sample.txt", "r") as file:
    content = file.read()
upper = 0
lower = 0
for ch in content:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase characters:", upper)
print("Lowercase characters:", lower)
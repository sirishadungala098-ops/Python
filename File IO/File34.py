with open("sample.txt", "r") as file:
    content = file.read()
count = 0
for ch in content:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1
print("Total consonants:", count)
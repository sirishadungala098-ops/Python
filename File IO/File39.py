word = input("Enter word: ")
with open("sample.txt", "r") as file:
    for line in file:
        if word in line:
            print(line, end="")
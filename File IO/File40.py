char = input("Enter character: ")
with open("sample.txt", "r") as file:
    for line in file:
        if line.startswith(char):
            print(line, end="")
file = open("sample.txt", "w")
lines = ["Hello\n", "Python\n", "Welcome"]
file.writelines(lines)
file.close()
print("Multiple lines written")
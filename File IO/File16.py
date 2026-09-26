import os

if not os.path.exists("newfile.txt"):
    file = open("newfile.txt", "x")
    file.write("This is a new file")
    file.close()
    print("File created")
else:
    print("File already exists")
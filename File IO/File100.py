import os
while True:
    print(" File Management System ")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Add Content")
    print("5. Delete File")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        filename = input("Enter filename: ")
        try:
            with open(filename, "x") as file:
                print("File created successfully")
        except FileExistsError:
            print("File already exists")
        except PermissionError:
            print("Permission denied")
    elif choice == "2":
        filename = input("Enter filename: ")
        content = input("Enter content: ")
        try:
            with open(filename, "w") as file:
                file.write(content)
            print("Content written successfully")
        except PermissionError:
            print("Permission denied")
    elif choice == "3":
        filename = input("Enter filename: ")
        try:
            with open(filename, "r") as file:
                print("\nFile Content:")
                print(file.read())
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Permission denied")
    elif choice == "4":
        filename = input("Enter filename: ")
        content = input("Enter content: ")
        try:
            with open(filename, "a") as file:
                file.write("\n" + content)
            print("Content added successfully")
        except FileNotFoundError:
            print("File not found")
        except PermissionError:
            print("Permission denied")
    elif choice == "5":
        filename = input("Enter filename: ")
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print("File deleted successfully")
            else:
                print("File does not exist")
        except PermissionError:
            print("Permission denied")
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
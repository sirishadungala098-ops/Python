try:
    with open("source.txt", "r") as source:
        content = source.read()
    with open("destination.txt", "w") as destination:
        destination.write(content)
    print("File copied successfully")
except FileNotFoundError:
    print("Source file not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print("Error:", e)
import json
try:
    with open("students.json", "r") as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError:
    print("Invalid JSON data")
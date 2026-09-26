import json
employees = [
    {
        "id": 1,
        "name": "John",
        "salary": 50000
    },
    {
        "id": 2,
        "name": "Anu",
        "salary": 60000
    },
    {
        "id": 3,
        "name": "Ravi",
        "salary": 55000
    }
]
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
print("Employee JSON file created")
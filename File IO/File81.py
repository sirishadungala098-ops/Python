import json

students = [
    {
        "id": 101,
        "name": "John",
        "course": "Python",
        "marks": 85
    },
    {
        "id": 102,
        "name": "Anu",
        "course": "Java",
        "marks": 78
    }
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print("JSON file created")
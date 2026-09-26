import json
student = {
    "id": 101,
    "name": "John",
    "course": "Python",
    "marks": 85
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("Dictionary converted to JSON file")
import json
with open("employees.json", "r") as file:
    employees = json.load(file)
highest = employees[0]
for employee in employees:
    if employee["salary"] > highest["salary"]:
        highest = employee
print("Employee:", highest["name"])
print("Highest salary:", highest["salary"])
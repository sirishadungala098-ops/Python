def topper(marks):
    topper_name = ""
    highest = 0
    for name, mark in marks.items():
        if mark > highest:
            highest = mark
            topper_name = name

    return topper_name
marks = {
    "Sirisha": 85,
    "Raghu": 92,
    "Janu": 88,
    "Sri": 78
}
print("Topper:", topper(marks))
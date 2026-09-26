def greater_than_50(data):
    result = []
    for key, value in data.items():
        if value > 50:
            result.append(key)
    return result
marks = {
    "Html": 75,
    "Java": 45,
    "C": 65,
    "Python": 90
}
print(greater_than_50(marks))
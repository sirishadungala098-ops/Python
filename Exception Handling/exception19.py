student = {
    "name": "Sirisha",
    "age": 21,
    "course": "Python"
}
try:
    key = input("Enter key: ")
    print("Value:", student[key])
except KeyError:
    print("Key not found")
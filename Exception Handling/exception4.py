try:
    student = {"name": "Sirisha", "age": 21}
    print(student["marks"])
except KeyError:
    print("Key does not exist")
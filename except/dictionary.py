student = {
    "id":101,
    "name":"siri",
    "course":"ccn"
}
try:
    key=input("enter student details:")
    print(student[key])
except KeyError:
    print("missing dictionary key")
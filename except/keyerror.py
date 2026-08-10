student={
    "name":"siri",
    "course":"python"
}
try:
    print(student["branch"])
except KeyError:
    print("keyy does not exist")
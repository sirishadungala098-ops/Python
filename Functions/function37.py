def student_details(*args, **kwargs):
    print("Student Details:")
    for value in args:
        print(value)
    print("Marks:")
    for subject, mark in kwargs.items():
        print(subject, ":", mark)
student_details(
    "Sirisha",
    21,
    "Python",
    Python=90,
    SQL=85,
    JavaScript=88
)
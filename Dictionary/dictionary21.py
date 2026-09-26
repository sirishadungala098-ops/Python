student={
    "Siri":86,
    "Sravya":90,
    "Bhagya":80,
    "Ramya":60
}
topper=max(student,key=student.get)
lowest=min(student,key=student.get)
print("Topper student",student[topper])
print("Lower student",student[lowest])
marks={
   "Sirisha":90,
   "Tanu":89,
   "Sri":95,
   "Bhagya":80
}
highest_student=""
highest_marks=0
for student, mark in marks.items():
    if mark > highest_marks:
        highest_marks=mark
        highest_student=student
print("Highest marks",highest_student,highest_marks)
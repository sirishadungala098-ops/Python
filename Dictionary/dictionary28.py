sub1={
    "Harshini":90,
    "Varsha":80,
    "Harini":86,
    "Vyshu":76
}
sub2 = {
    "Varsha":90,
    "Jaanu":80,
    "Yamuna":70,
    "Harini":86,
    "Vyshu":85
}

students=set(sub1.keys()) & set(sub2.keys())
print(students)
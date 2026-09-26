employees={
    "Sirisha":45000,
    "Bhagya":55000,
    "Sravan":35000,
    "Tanuu":75000
}
total=0
for salary in employees.values():
    total+=salary
average=total/len(employees)
print("average salary",average)
emp=[("Sravan","Teaching",50000),("Varsha","Teaching",45000),("Teju","Technician",35000)]
highest=0
for i in emp:
    Name,Designation,salary=i;
    if highest < salary :
        highest=salary
print("Highest salary :", highest);

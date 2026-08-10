courses = ["Python", "Java", "Data Science"]
try:
    index = int(input("Enter course index: "))
    print("Selected course:", courses[index])
except ValueError:
    print("Enter an integer index")
except IndexError:
    print("not found")
email= input("Enter email address:") 
if "@" in email and "." in email:
    print(" Email format is valid")
else:
    print("Invalid email format")
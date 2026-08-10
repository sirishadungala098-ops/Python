name = input("Enter your name: ").strip() 
if name.replace(" ", "").isalpha():
    print("Valid Name") 
else:
    print("Name should contain letters only")
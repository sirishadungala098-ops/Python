save_username = "sirisha"
save_password = "bhagya@123"
username = input("Enter username:").strip()
password = input("Enter password:") 
if username == save_username and password == save_password:
    print("Login Successful")
else:
    print("Invalid Username")
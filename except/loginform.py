correct_username="siri"
correct_password="python"
try:
    username=input("Enter username:")
    password=input("Enter password:")
    if username!=correct_username:
        raise ValueError("invalid username")
    if password!=correct_password:
        raise ValueError("invalid password")
except ValueError as e:
    print("login failed",e)
else:
    print("login successfullyy")
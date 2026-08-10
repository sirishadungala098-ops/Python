email="siridungala@example.com"
username, domain = email.split("@") 
masked = username[0] + "***@" + domain 
print(masked)
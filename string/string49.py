s=input("Enter a string:")
reverse=""
for char in s:
    reverse=char+reverse
if s==reverse:
    print("palindrome")
else:
    print("Not a palindrome")
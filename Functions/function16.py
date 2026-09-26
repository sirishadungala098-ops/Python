def palindrome(n):
    if str(n) == str(n)[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
num=int(input("Enter a number:"))
print(palindrome(num))
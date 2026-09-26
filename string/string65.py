s1=input("Enter a first string:")
s2=input("Enter second string:")
if sorted(s1)==sorted(s2):
    print("It is an anagram")
else:
    print("Not an anagram")
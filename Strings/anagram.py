word1=input("enter word1:").lower()
word2=input("enter word2:").lower()
if sorted(word1)==sorted(word2):
    print("Anagram")
else:
    print("Not an anagram")
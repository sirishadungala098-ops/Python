sentence = input("Enter sentence: ")
words = sentence.split() 
shortest = max(words,key=len)
print("Shortest Word:",shortest)
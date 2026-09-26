word="python is easy to learn"
smallest=" "
for word in word.split():
    if len(word)<len(smallest):
        smallest=word
print("smallest word")
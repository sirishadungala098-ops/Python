word="python is easy to learn"
largest=" "
for word in word.split():
    if len(word)>len(largest):
        largest=word
print("largest word")
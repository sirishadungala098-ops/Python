s="python is easy and it is easy to learn"
words=s.split()
result=[]
for word in words:
    if word not in result:
        result.append(word)
print(" ".join(result))

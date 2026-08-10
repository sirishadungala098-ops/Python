sentence="python is a easy and very powerful language"
word=sentence.split()
frequency={}
for word in word:
    if word in frequency:
         frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)    

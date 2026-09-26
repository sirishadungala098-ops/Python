a="java is very powerful language"
for char in a:
    if a.count(char)==1:
        print("First non-repeated character",char)
        break
print(char)
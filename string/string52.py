a="java is very powerful language"
seen=set()
for char in a:
    if char in seen:
        print("First repeated character",char)
        break
    seen.add(char)
else:
    print("No repeated characters",char)
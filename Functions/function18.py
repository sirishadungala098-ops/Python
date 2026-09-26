def vowels(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count = count + 1
    return count
s = input("Enter a string: ")
print(vowels(s))
s="python is easy to learn language"
consonants_count=0
vowels="aeiou"
for  character in s:
    if  character.isalpha() and character not in vowels:
        consonants_count += 1
print(consonants_count)
    
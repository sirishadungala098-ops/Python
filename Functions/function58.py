def character_frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    return frequency
text = "hello"
print(character_frequency(text))
text="python@123#hello*!"
specials=" "
for character in text:
    if not character.isalnum() and not character.isspace():
        specials+=character
print(specials)
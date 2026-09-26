numbers={
    "a":1,
    "b":20,
    "c":33,
    "d":11,
    "e":21,
    "f":22,
    "g":40
}
even_count=0
odd_count=0
for value in numbers.values():
    if value%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even num counts",even_count)
print("Odd num counts",odd_count)
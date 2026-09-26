positive = 0
negative = 0
zero = 0
with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line)
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
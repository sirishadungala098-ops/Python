import math
try:
    result=math.exp(1000)
except OverflowError:
    print("Result is too large")
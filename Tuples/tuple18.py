data=(
    [10,20,30,40],
    ["Apple","Banana","Mango","Cherry"],
    [True,False,True,False],
)
print(data[0][1])
print(data[1][2])
print(data[2][1])

data[0][1]=60
data[1][2]="Strawberry"
data[2][1]=True
print(data)
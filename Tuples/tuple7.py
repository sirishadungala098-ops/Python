c=(10,20,40,30,31,21,23)
l=10
s=c[0]
for i in c:
    if i>l:
        l=i
    if i<s:
        s=i
print(l)             
print(s)

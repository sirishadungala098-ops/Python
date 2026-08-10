try:
    l1=[10,20,"abc",4.8,True]   
    ind=int(input("Enter index value:"))
    print(l1[ind])
except IndexError as i:
    print("invalid list index",i)
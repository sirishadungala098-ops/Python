try:
   x=int(input("Enter x value:"))
   y=int(input("Enter y value:"))
   z=x/y
   print(z)
   print("end program")
   print("rest of the line")
except ZeroDivisionError as e:
   print("Error:",e)
x=int(input("enter the length"))
y=int(input("enter the length"))
z=int(input("enter the length"))
if (x==y==z):
    print("equilateral triangle")
elif(x==y) or (x==z) or (y==z):
    print("isosceles triangle")
else:
    print("scalene triangle")
    
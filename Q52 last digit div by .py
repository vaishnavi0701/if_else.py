
x=int(input("enter no:"))
a=x%10
if x>1:
    print(a)
    if a%3==0:
        print("last digit div by 3")
    else:
        print("not div")
else:
    print("not last digit")


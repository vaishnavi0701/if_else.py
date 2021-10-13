x=int(input("enter month number"))
if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
    print("31 days")
elif x==2:
    print("28 or 29 days")
elif x==4 or x==6 or x==9 or x==11:
    print("30 days")
else:
    print("nothing")
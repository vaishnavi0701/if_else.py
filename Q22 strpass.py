x=input("enter the password")
if x>="a" and x<="z" or x>="A" and x<="Z":
    if x==1 or x==2 or x==3 or x==4 or x==5 or x==6 or x==7 or x==8 or x==9 or x==0:
        if x=="@" or x=="#" or x=="$" or x=="&": 
            print("correct password")
        else:
            print("incorrect password")
    else:
        print("invalid entered password")
else:
    print("invalid password")
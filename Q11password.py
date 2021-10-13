a=input("enter alphabet")
b=input("enter special characters")
c=int(input("enter number"))
if a>="A" and a<="Z"or a>="a" and a<="z":
    if b=="@"or"#"or"$"or"&":
        if c=="1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or"0":
            print("correct password")
        else:
            print("wrong password")
    else:
        print("wrong password")
else:
    print("wrong password")
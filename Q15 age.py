n=input("enter age")
n=int(input("enter age"))
if n>5<18:
    print("you can go to school")
    if n>18<21:
        print("you can vote")
    if n>21<24:
        print("you can drive car")
    if n>24<25:
        print("you can do marriage")
    if n>25:
        print("you can drink legally")
else:
    print("rest of code")
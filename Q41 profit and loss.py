a=int(input("selling price"))
b=int(input("cost price"))
if a>b:
    print(a-b,"profit")
elif a<b:
    print(b-a,"loss")
elif a==b:
    print("no profit no loss")
else:
    print("nothing")
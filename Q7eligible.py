age=int(input("enter age"))
if age>=50:
    print("person is eligible")
else:
    if age>40:
        disease=int(input("enter1=disease,0=no disease"))
        if disease==1:
            print("person is eligible")
        else:
            print("wait for your turn")
    else:
        print("wait for your turn")


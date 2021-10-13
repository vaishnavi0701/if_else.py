num1=int(input("enter number"))
num2=int(input("enter number"))
num3=int(input("enter number"))
if ((num1>num2)*num1+(num2>num1)*num2)==num1:
    if ((num1>num3)*num1+(num3>num1)*num3)==num1:
        print(num1)
elif ((num1>num2)*num1+(num2>num1)*num2)==num2:
    if ((num2>num3)*num2+(num3>num2)*num3)==num2:
        print(num2)
else:
    print(num3)
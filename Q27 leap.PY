x=int(input("enter the year"))
if (x%4==0 and x%100!=0 or x%400==0):
    print(("it is a leap year"))
else:
    print("it is not leap year")

day=int(input("enter the date :"))
month=int(input("enter the month :"))
year=int(input("enter the year :"))

if(year%4==0 and year%100!=0) or year%400==0:
    if(month==2):
      (day>=1 and day<=29)
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        (day>=1 and day<=31 )
    else:
        (day>=1 and day<=30)
else:
    if(month==2):
      (day>=1 and day<=28)
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
       (day>=1 and day<=31 )
    else:
        (day>=1 and day<=30)
if(year%4==0 and year%100!=0) or year%400==0:
    if(month==2): 
      (day==29)
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
      (day==31)
    else:
        day=30
        (month==month+1)
elif(day==31 and month==12):
    day=1
    month=1
    year=year+1
else:
    day=day+1
print(day,"/",month,"/",year,)


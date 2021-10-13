days=int(input("enter the  days"))
if days==31:
    print("january","may","march","july","august","october","december")
elif days==30:
    print("april","june","september","november")
elif days==28 or days==29:
    print("february")
else:
    print("nothing")

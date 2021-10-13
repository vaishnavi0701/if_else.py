user=int(input("enter the capacity of water in l"))
if (user<1):
    print("put water")
elif(user>=10):
    print("overflow")
else:
    print("dont put water")
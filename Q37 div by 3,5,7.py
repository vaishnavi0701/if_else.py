user=int(input("enter the number"))
if user%3==0:
    print("fizz")
elif user%5==0:
    print("buzz")
elif user%7==0:
    print("fizzbuzz")
else:
    print("nothing")
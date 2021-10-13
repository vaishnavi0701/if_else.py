print("Wel Come SBI")
a=input("Select Your Language-")
if a=="English":
	print("English")
print("Enter Two Digit Number")
A=int(input("10 to 99  -- "))
if A>=10 and A<=99:
	print("Ok then Next Go")
	print("Plese Swip your card")
else:
	print("Plese Enter two digit Number")
print("Plese Enter Your Best Pin")
B=int(input("**"))
if (B>=0000 or B==1234 )and (B<=9999 or B==4567):
	print(''' 
	            1)  Balance Enquiry 
	            2)  Cash Withdrwal
	            3)  Deposit
	            4)  Exit
	         ''')
else :
    	print("Invalid Pin")
balance=10000
Enquiry=int(input(""))
Amount=balance - Enquiry
if Enquiry==1:
	print("Your Balance is", balance)
	
elif Enquiry==2:
	wid=int(input("Please Enter Your Amount - "))
	print("Your balance is",balance-wid)
	print("Please Collect yor Amount")
elif Enquiry==3:
	print("Previous Amount is",balance)
	Dep=int(input("Enter Your Deposit Amount -  "))
	print("Your Deposit Amount is",balance+Dep)
elif Enquiry==4:
	print("Thanks For Visiting SBI")
	exit()            
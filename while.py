p = int(input("Please input number between 1 and 12: "))

while p < 1 or p > 12:
	print ("Invalid.\n")
	p = int(input("Please input number between 1 and 12: "))

print ("Number is",p)


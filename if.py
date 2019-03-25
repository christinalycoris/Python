#switch equivalent

m = int(input("Please enter a number between 1 and 12: "))

if m == 1:
	print ("The first month of the year is January.\n")
elif m == 2 or m == 3:
	print ("The month is either February or March.\n")
elif m == 4 or m == 5 or m == 6:
	print ("The month is April, May, or June.\n")
elif m == 7 or m == 8 or m == 9:
	print ("The month is July, August, or September.\n")
elif m == 10 or m == 11:
	print ("The month is either October or November.\n")
elif m == 12:
	print ("The last month of the year is December.\n")
else:
	print ("Hmm. I don't seem to know that one.\n")


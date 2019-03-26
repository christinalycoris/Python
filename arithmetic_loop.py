import math

print ("This program will compute addition, subtraction,\n"
		"multiplication, or division. The user will\n"
		"provide two inputs. The inputs could be any real\n"
		"numbers. This program will not compute complex\n"
		"numbers. The program will run until the user\n"
		"chooses to terminate the program. The user can\n"
		"do this by selecting the appropriate option when\n"
		"prompted to do so.\n\n")

ans = input("Do you want to continue? Y/N ")

while ans == 'Y' or ans == 'y' or ans == 'Yes' or ans == 'yes' or ans == 'YES':
	print ("\nSelect one operation: ")
	print ("\t1. Addition ")
	print ("\t2. Subtraction (A from B) ")
	print ("\t3. Subtraction (B from A) ")
	print ("\t4. Multiplication ")
	print ("\t5. Division (A into B) ")
	print ("\t6. Division (B into A) ")
	print ("\t7. EXIT ")
	sel = int(input("Your selection is: "))

	while sel < 1 or sel > 6:
		if sel == 7:
			print ("Okay. Goodbye. \n")
			exit()
		else:
			print ("Invalid.\n")
			sel = int(input("Your selection is: "))

	print ("\n")

	x = float(input("Input a (all real numbers): "))
	y = float(input("Input b (all real numbers): "))

	print ("\n")

	if sel == 1:
		print ("1. Addition \n\t",x,"+",y,"=",x+y)
	elif sel == 2:
		print ("2. Subtraction (A from B) \n\t",y,"-",x,"=",y-x)
	elif sel == 3:
		print ("3. Subtraction (B from A) \n\t",x,"-",y,"=",x-y)
	elif sel == 4:
		print ("4. Multiplication \n\t",x,"×",y,"=",x*y)
	elif sel == 5:
		print ("5. Division (A into B) \n\t",y,"÷",x,"=",y/x)
	elif sel == 6:
		print ("6. Division (B into A) \n\t",x,"÷",y,"=",x/y)
	else:
		print ("Hmm. I don't seem to know that one.\n")

if ans == 'N' or ans == 'n' or ans == 'No' or ans == 'no' or ans == 'NO':
	print ("\nOkay. Goodbye. \n")
	exit()


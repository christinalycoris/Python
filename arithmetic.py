import math

print ("Select one operation: ")
print ("\t1. Addition ")
print ("\t2. Subtraction (A from B) ")
print ("\t3. Subtraction (B from A) ")
print ("\t4. Multiplication ")
print ("\t5. Division (A into B) ")
print ("\t6. Division (B into A) ")
sel = int(input("Your selection is: "))

while sel < 1 or sel > 6:
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


print ("This program will determine if the number the user inputs\n"
	"into the program is even or odd (or neither). Integers only.")
ans = input("Do you want to continue? Y/N ")

while 'Y' in ans or 'y' in ans:
	num = int(input("Enter a number: "))
	if num == 0:
		print("The number zero is neither even nor odd.")
	elif (num % 2) == 0:
		print("{0} is even".format(num))
	else:
		print("{0} is odd".format(num))
	ans = input("Do you want to continue? Y/N ")

while 'N' in ans or 'n' in ans: #could also use 'if' in place of 'while'
	print('That\'s too bad. :(\nGoodbye.')
	exit()


num = int(input("Enter a number: "))

if num == 0:
	print("{0} is neither even nor odd.".format(num))
elif (num % 2) == 0:
	print("{0} is even.".format(num))
else:
	print("{0} is odd.".format(num))


n = int(input("Please enter a number: "))

counter = 0
product = 1

for i in range(1,n+1,1):
	product = product * i
	counter += 1
	if i > n:
	    break
	print(i, end=" × ")
print("END")
print("The product of " + str(n) + "! is " + str(product) )


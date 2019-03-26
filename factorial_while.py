n = int(input("Please enter a number: "))

counter = 0
product = 1
i = 1

while i <= n:
	product = product * i
	counter += 1
	if i > n:
	    break
	print(i, end=" × ")
	i+=1

print("END")
print("The product of " + str(n) + "! is " + str(product) )


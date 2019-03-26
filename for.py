j = int(input("Please enter a starting number: "))
k = int(input("Please enter an ending number: "))
n = int(input("Please enter an increment number: "))

count=0
fin=k+n

print("Your numbers are: ", end="")

for i in range(j,fin,n):
	if i > k:
	    break
	count += 1
	print(i, end=" ")

print("\nThere are",count,"numbers.")


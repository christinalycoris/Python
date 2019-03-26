j = int(input("Please enter a starting number: "))
k = int(input("Please enter an ending number: "))
n = int(input("Please enter an increment number: "))
sum = 0
counter = 0
fin=k+n

for i in range(j,fin,n):
	sum = sum + i
	counter += 1
	if i > k:
	    break
	print(i, end=" + ")
	#python 2.X is 
	#print "this will be on",
	#print "the same line"
print("END LOOP")
print("Sum from",j,"to",k,"is",sum)
print("There are",counter,"numbers in the series.")


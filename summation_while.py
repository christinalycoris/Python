j = int(input("Please enter a starting number: "))
k = int(input("Please enter an ending number: "))
n = int(input("Please enter an increment number: "))

sum=0
count=0

while j <= k:
    sum = sum+j
    print(j, end=" + ")
    j = j+n
    count+=1
    if j > k:
        break
print('Loop ended.')
print('Sum of series is', sum)
print('Loop ran',count,'times.')



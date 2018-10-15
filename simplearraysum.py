# this program is to find the of numbers in an array
# first it takes number of elements in an array
# then it takes list of elements in an array
# finally finds their sum
n=int(input("enter number of elements "))
ar=list(map(int, input().strip().split(" ")))
sum=0
for i in range(0,n):
	sum=sum+ar[i]
print(sum,"is sum of elements")

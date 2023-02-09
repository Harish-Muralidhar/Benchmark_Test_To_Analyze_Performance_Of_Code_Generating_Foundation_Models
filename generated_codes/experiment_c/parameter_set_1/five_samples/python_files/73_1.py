
Explanation:
Example case 1. One of the possible pair of beat notations is (2, 5, 8, 11) and (2, 4, 8, 16).
Example case 2. One of the possible pair of beat notations is (1, 2, 3, 4, 5) and (2, 4, 8, 16, 32)
Example case 3. One of the possible pair of beat notations is (1, 2, 4, 8) and (1, 3, 9, 27)

Solution:

def find_ap(arr):
	#finding the common diff
	cd=arr[1]-arr[0]

	ans=[]
	ans.append(arr[0])

	for i in range(1,len(arr)):
		ans.append(arr[i-1]+cd)
	return ans

def find_gp(arr):
	cd=arr[1]/arr[0]
	ans=[]
	ans.append(arr[0])

	for i in range(1,len(arr)):
		ans.append(int(arr[i-1]*cd))
	return ans

def find_both(a,b):
	i=0
	j=0

	while(i<len(a) and j<len(b)):
		if a[i]==b[j]:
			print(a[i],end=' ')
			i+=1
			j+=1
		elif a[i]<b[j]:
			i+=1
		else:
			j+=1
	print()


t=int(input())

while(t>0):
	t-=1
	n=int(input())
	arr=list(map(int,input().split()))
	a=find_ap(arr)
	b=find_gp(arr)
	find_both(a,b)
	for i in a:
		print(i,end=' ')
	print()
	for i in b:
		print(i,end=' ')
	print()
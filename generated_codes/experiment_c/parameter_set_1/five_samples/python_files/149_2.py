'''

Solution:
'''
for i in range(int(input())):
	a = int(input())
	b = list(map(int,input().split()))
	x,y = b[0],b[0]
	for j in b:
		if j > y:
			x += j-y
			y = j
		elif j < y:
			y = j
	print(x)
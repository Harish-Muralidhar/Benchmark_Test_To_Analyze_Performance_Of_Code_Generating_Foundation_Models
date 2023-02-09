'''
Example case 2. In this example 2 as 20 is greater than 10.
Example case 3. In this example 3 as 10 is equal to 10.

'''

def relationshipCheck(a,b):
	if a>b:
		return '>'
	elif a<b:
		return '<'
	else:
		return '='

t=int(input())
for i in range(t):
	a,b=map(int,input().split())
	print(relationshipCheck(a,b))
'''


'''


def factor(n,p):
	fact = 1
	for i in range(0,p):
		fact = fact*(n-i)
	return fact

def function(n,k):
	fact = 1
	for i in range(0,p):
		fact = fact*(n-i)
	return fact

def nCr(n,r):
	return factor(n,r)//factor(r,0)

t = int(input())
for _ in range(t):
	n,k = map(int,input().split())
	res = 0
	for i in range(1,n):
		res = res + nCr(n,i)*k**(n-i)*(k-1)**i
	res = res + (k**n)
	print(res%(10**9 + 7))
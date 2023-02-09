

import math 
def gcd(a, b): 
	if (a == 0): 
		return b 
	return gcd(b % a, a) 
def lcm(a, b): 
	return (a*b) / gcd(a, b) 
test = int(input())
for t in range(test):
	a, b = map(int, input().split())
	print(int(gcd(a, b)), int(lcm(a, b)))
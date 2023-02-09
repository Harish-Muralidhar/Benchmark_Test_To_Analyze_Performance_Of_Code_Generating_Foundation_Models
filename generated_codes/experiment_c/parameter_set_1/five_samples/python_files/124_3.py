"""

"""

def reverse(string):
	return string[::-1]

def binar(n):
	return bin(n)[2:]

def flip(string):
	flipped=[]
	for i in string:
		if i=='0':
			flipped.append('1')
		if i=='1':
			flipped.append('0')
	return "".join(flipped)

def todec(string):
	return int(string,2)

tests=int(input())
for i in range(tests):
	k,s=input().split(" ")
	k=int(k)
	s=list(s)
	for i in range(len(s)):
		n=binar(i)
		while len(n)<k:
			n="0"+n
		if len(n)>k:
			n=n[len(n)-k:]
		n=flip(n)
		index=todec(n)
		s[index]=s[i]
	print("".join(s))
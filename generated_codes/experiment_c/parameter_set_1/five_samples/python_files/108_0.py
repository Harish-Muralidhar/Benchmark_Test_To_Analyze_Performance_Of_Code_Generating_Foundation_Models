/*

Input:
1
1

Output:
1

*/

T=int(input())

for x in range(T):
	N=int(input())

	i=1
	s=set()
	c=0
	while(1):
		if(i not in s):
			s.add(i)
			c+=1
			if(i==N):
				break
		i+=1

	print(c)
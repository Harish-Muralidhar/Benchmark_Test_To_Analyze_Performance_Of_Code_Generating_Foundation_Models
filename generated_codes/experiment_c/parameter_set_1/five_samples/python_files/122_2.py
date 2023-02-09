'''


'''

n = int(input())
K = []
for i in range(n):
	K.append(int(input()))

for i in range(n):
	k = K[i]
	if k==0:
		print(3)
	temp = [3,1,3,3,2,3]
	for i in range(k-6):
		temp.append(1)
	temp.append(2)
	temp.append(1)
	for i in range(k-6):
		temp.append(2)
	print(str(temp[0])+'.',end="")
	for i in range(1,len(temp)):
		print(str(temp[i]),end="")
	print()
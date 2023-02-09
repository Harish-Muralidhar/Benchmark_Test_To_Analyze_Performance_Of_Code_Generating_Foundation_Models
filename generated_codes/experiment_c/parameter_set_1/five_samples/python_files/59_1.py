'''


'''




def countSeq(arr, n):
	ans = 1
	for i in range(n):
		ans = ans + 2**(i+1)
	print(ans)

T = int(input())
for t in range(T):
	N = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	countSeq(arr, N)
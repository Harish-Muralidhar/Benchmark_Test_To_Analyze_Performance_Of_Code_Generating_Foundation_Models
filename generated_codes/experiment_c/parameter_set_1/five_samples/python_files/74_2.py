'''

Explanation

In the first test case the only progression is (2, 4, 6). In the second test case the total number of progressions is one. In the last test case the progressions are (5, 14, 23, 32), (6, 15, 24, 33) and (8, 16, 24, 32).

Note: The input will be large, so you need to use faster I/O methods. 

'''

def max_len_prog(l,r,k):
	ans = 1
	i = l
	j = l+k
	while j<=r:
		temp = 1
		while j<=r and i+k == j:
			temp += 1
			i += k
			j += k
		ans = max(ans, temp)
		i += 1
		j += 1
	return ans


def get_nth_prog(l,r,k,n):
	#print l,r,k,n
	ans = []
	i = l
	j = l+k
	while j<=r:
		temp = [(i,j)]
		while j<=r and i+k == j:
			temp.append((i,i+k))
			i += k
			j += k
		if len(temp) > 2:
			ans.append(temp)
		i += 1
		j += 1

	if len(ans) < n:
		return 0,0
	else:
		ans = reduce(lambda x,y:x+y, ans)
		ans = sorted(ans, key = lambda x:(x[0],x[1]))
		#print ans
		return ans[n-1][0],ans[n-1][1]



def main():
	t = int(raw_input())
	for i in range(t):
		L,R,k,n = map(int,raw_input().split())
		len_prog = max_len_prog(L,R,k)
		#print len_prog
		print len_prog,
		print get_nth_prog(L,R,k,n)


if __name__ == '__main__':
	main()
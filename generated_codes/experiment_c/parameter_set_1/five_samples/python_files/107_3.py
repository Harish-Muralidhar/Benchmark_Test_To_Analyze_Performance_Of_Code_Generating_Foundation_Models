'''
'''

import numpy as np

def solution(num,steps):
	ans = [sum(num[:i]) - sum(num[i:]) for i in steps]
	return ans

if __name__ == '__main__':
	n,m = 10,3
	num = [3,2,4,1,5,2,3,9,7]
	steps = [1,4,7]
	ans = solution(num,steps)
	print(ans)
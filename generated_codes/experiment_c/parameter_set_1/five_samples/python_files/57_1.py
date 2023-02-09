'''

Test Case 3: The ways the chef can place the rooks initially are given below. The ways that are marked in bold below are those in which the Sous Chef cannot win.

1 1
0 1

1 0
1 0

1 0
0 1

2 0
0 1

2 0
1 0

0 2
1 0

0 2
0 1

0 1
0 2

0 1
2 0

1 0
2 0

1 0
0 2
Test Case 4: The ways the chef can place the rooks initially are given below. The ways that are marked in bold below are those in which the Sous Chef cannot win.

2 0
2 0

2 0
0 2

0 2
2 0

0 2
0 2

1 1
1 1

1 1
0 2

1 1
2 0

1 0
1 0

1 0
2 1

1 0
1 1

1 0
0 2

1 0
2 0

0 1
0 1

0 1
1 0

0 1
1 1

0 1
0 2

0 1
2 0

0 2
1 1

0 2
0 1

0 2
2 0

0 2
1 0

1 0
0 1

1 0
2 1

1 0
1 1

1 0
0 2

1 0
2 0

2 1
1 0

2 1
0 1

2 1
1 1

2 1
0 2

2 1
2 0

2 0
1 1

2 0
0 1

2 0
2 0

2 0
0 2

1 1
2 1

1 1
1 0

1 1
0 1

1 1
2 0

1 2
1 0

1 2
2 0

1 2
0 1

1 2
1 1

1 2
2 1

1 2
0 2

1 2
1 2

1 2
2 2

1 2
2 1

2 2
1 1

2 2
0 1

2 2
1 0

2 2
2 0

2 2
0 2

2 2
2 1

2 2
1 2



Solution:
'''

import math
def count_solutions(r,c,n):
	if n==0:
		return 1
	elif r==0 or c==0:
		return 0
	else:
		return count_solutions(r-1,c,n) + count_solutions(r,c-1,n) - count_solutions(r-1,c-1,n-1)

def main():
	T=int(input())
	for i in range(T):
		r,c,n=list(map(int,input().split()))
		print(count_solutions(r,c,n))

if __name__ == '__main__':
	main()
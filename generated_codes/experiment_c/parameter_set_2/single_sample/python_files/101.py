'''


Explanation

The first test case has a beanstalk with 3 levels, and the number of leaves at each level is 0, 1, 2. This is a valid beanstalk.

The second test case has a beanstalk with 3 levels, and the number of leaves at each level is 0, 0, 3. This is not a valid beanstalk, because at level 2 there are no stems, and hence no leaves at level 3.

'''

import sys

def main():
	test_cases = int(sys.stdin.readline().strip())
	for i in range(test_cases):
		num_levels = int(sys.stdin.readline().strip())
		leaves = map(int, sys.stdin.readline().strip().split())
		#print leaves
		if num_levels == 1:
			if leaves[0] == 1:
				print "Yes"
			else:
				print "No"
			continue
		if leaves[0] != 0:
			print "No"
			continue
		if leaves[num_levels-1] != 1:
			print "No"
			continue
		if leaves[num_levels-2] == 0:
			print "No"
			continue
		for j in range(1,num_levels-1):
			if leaves[j] > leaves[j-1]*2:
				print "No"
				break
		else:
			print "Yes"
			
if __name__ == "__main__":
	main()
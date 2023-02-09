'''
NOT INDIAN
Explanation
First person is definitely not Indian because he uses the "No" gesture.
Second person uses "Yes" gesture twice and "Indian Yes" gesture once. This could be an Indian or a foreigner who has picked up the Indian way.
Third person is definitely Indian.
Fourth person is definitely not Indian.
'''

# Python3 program to find whether a given 
# person is indian or not 
import math 

# function to find whether a person is 
# indian or not 
def indianOrNot(s, n): 

	# if total length of string is less 
	# than 2 then it cannot be indian 
	if (n < 2): 
		return False

	# To store occurrences of I and N. 
	inCount = 0

	# To store occurrences of Y and N. 
	ynCount = 0

	# To store occurrences of I and Y. 
	iyCount = 0

	for i in range(n): 

		# If any of the 
		# condition is true 
		# then it is not Indian 
		if (s[i] == 'Y' and (inCount or iyCount)): 
			return False

		if (s[i] == 'N' and (iyCount)): 
			return False

		# If I is found then 
		# increment inCount and 
		# increment ynCount by 
		# previous value of inCount 
		if (s[i] == 'I'): 
			inCount += 1
			ynCount += inCount

		# If Y or N is found then 
		# increment ynCount and 
		# increment iyCount by 
		# previous value of ynCount 
		elif (s[i] == 'Y' or s[i] == 'N'): 
			ynCount += 1
			iyCount += ynCount 

	return True

# Driver code 
if __name__ == '__main__': 

	# string of I, N and Y 
	s = "YYIN"
	n = math.floor(len(s)) 

	if (indianOrNot(s, n)): 
		print("INDIAN") 
	else: 
		print("NOT INDIAN") 

# This code is contributed by Rituraj Jain
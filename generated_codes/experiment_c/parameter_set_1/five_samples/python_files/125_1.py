'''
Example case 2. In the first turn Sasha will choose 4 and boy will choose 3. In the second turn Sasha will choose 3 and boy will choose 4. So the answer will be 2. 
Example case 3. Sasha will always choose 2. The probability of the 2^2>2^2 is 0.5. So we can find answer as 0.5 + 0.5 = 1.
'''

import numpy as np

def main():
	t = int(input())
	while t:
		t-=1
		n = int(input())
		chefs = list(map(int, input().split()))
		sashas = list(map(int, input().split()))
		chefs.sort(reverse=True)
		sashas.sort(reverse=True)
		c = np.array(chefs)
		s = np.array(sashas)
		expected = 0
		for i in range(len(sashas)):
			# print(sashas[i])
			# print(chefs[i])
			if sashas[i]>chefs[i]:
				expected+=1
		print(expected)
		
if __name__ == "__main__":
	main()
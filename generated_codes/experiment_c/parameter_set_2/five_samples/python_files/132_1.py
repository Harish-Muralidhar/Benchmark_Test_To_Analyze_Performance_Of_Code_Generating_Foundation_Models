'''

Explanation

Initially, Harry grabs the book "english". Then he grabs the book "mathematics". Then he grabs the book "geography".

Harry wants to do a book exercise. He has to remove the book "geography" to pick the book "mathematics".

Harry grabs the book "graphics".

Harry wants to do a book exercise. He has to remove no books to pick the book "graphics".

'''

import heapq

def main():
	n = int(input())
	pile = []
	for i in range(n):
		action = input().split()
		if action[0] == '-1':
			if len(pile) == 0:
				continue
			else:
				print(len(pile) - 1, heapq.heappop(pile)[1])
		else:
			heapq.heappush(pile, (int(action[0]), action[1]))

if __name__ == '__main__':
	main()
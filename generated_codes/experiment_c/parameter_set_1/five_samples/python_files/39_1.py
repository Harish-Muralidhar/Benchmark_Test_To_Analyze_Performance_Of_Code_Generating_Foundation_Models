'''


'''

def find_max_coins(num_coins, max_people):
	if num_coins <= max_people:
		return num_coins
	else:
		return num_coins % max_people

T = int(input())
for _ in range(T):
	N, K = list(map(int, input().split()))
	print(find_max_coins(N, K))
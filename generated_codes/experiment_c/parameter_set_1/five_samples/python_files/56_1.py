'''

'''


import sys

def find_min_pos(N, K, start_pos, end_pos, pos_info):
	
	if start_pos not in pos_info:
		return start_pos
	elif end_pos not in pos_info:
		return end_pos
	elif pos_info[start_pos] > pos_info[end_pos]:
		return start_pos
	elif pos_info[start_pos] < pos_info[end_pos]:
		return end_pos
	else: #if pos_info[start_pos] == pos_info[end_pos]:
		if start_pos < end_pos:
			return start_pos
		else:
			return end_pos


def solution(N, K):

	pos_info = {}
	result = []
	for i in range(1, N+1):
		start_pos = i - K
		end_pos = i + K
		if start_pos < 1:
			start_pos = 1
		if end_pos > N:
			end_pos = N
		if start_pos <= end_pos:
			cur_pos = find_min_pos(N, K, start_pos, end_pos, pos_info)
			result.append(cur_pos)
			pos_info[cur_pos] = i

		else:
			return -1

	return result



if __name__ == '__main__':
	t = int(sys.stdin.readline())
	for i in range(t):
		data = sys.stdin.readline().split()
		N = int(data[0])
		K = int(data[1])
		print(' '.join(map(str, solution(N, K))))
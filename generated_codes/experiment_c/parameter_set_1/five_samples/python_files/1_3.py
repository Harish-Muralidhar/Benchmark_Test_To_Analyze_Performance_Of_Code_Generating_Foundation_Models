"""
"""

def get_sub_array_signs(arr, pos):
	sub_array = arr[pos:]
	sub_array_signs = []
	for i in sub_array:
		sub_array_signs.append(i > 0)
	return sub_array_signs

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		arr = [int(x) for x in input().split()]
		max_len_arr = []
		for j in range(n):
			sub_array_signs = get_sub_array_signs(arr, j)
			count = 0
			for k in range(len(sub_array_signs) - 1):
				if sub_array_signs[k] != sub_array_signs[k + 1]:
					count += 1
				else:
					break
			max_len_arr.append(count + 1)
		print(*max_len_arr)

if __name__ == "__main__":
	main()
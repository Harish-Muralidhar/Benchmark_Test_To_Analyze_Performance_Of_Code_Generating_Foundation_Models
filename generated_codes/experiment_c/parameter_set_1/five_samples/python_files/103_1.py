'''

'''


import math

def first_and_last_k_digits(n, k):
    num = int(math.pow(n, n))
    num_str = str(num)
    length = len(num_str)
    return (num_str[:k], num_str[length - k:])


t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    print(first_and_last_k_digits(n, k)[0], first_and_last_k_digits(n, k)[1])
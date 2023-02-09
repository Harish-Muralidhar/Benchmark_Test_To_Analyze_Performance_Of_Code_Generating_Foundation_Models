'''

Scoring

This problem is worth 10 points.

Explanation of sample

n=4, k=2.

4^4 = 256.

First two digits = 25, last two digits = 56.

n=9, k=3.

9^9 = 387420489.

First three digits = 387, last three digits = 489.

'''
import time

def power(a,b):
    if b==0:
        return 1
    if b%2==0:
        return power(a*a,b/2)
    else:
        return a*power(a*a,(b-1)/2)

def first_digits(a, b, k):
    a_to_b = power(a, b)
    num_digits_a_to_b = len(str(a_to_b))

    if num_digits_a_to_b <= k:
        return a_to_b

    first_digits = int(str(a_to_b)[:k])
    last_digits = int(str(a_to_b)[-k:])
    return (first_digits, last_digits)

if __name__ == '__main__':
    start_time = time.time()
    num_cases = int(raw_input())
    for i in range(num_cases):
        a, b, k = [int(j) for j in raw_input().split()]
        print '%d %d' % first_digits(a, b, k)
    print time.time() - start_time, "seconds"
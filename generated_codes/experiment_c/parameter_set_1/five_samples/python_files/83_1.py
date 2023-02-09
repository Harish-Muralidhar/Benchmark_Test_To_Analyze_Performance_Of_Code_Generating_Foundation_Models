'''

Explanation:
The sum of the first three numbers is 15 + 11 + 16 = 42 and the sum
of the last four numbers is 26 + 11 = 37.
Therefore, the answer is 42 mod 17 = 2.

Hint: Use queue.
'''

from __future__ import print_function
import collections

def pre_processing(n, k, p, array):
    '''
    fill the queue when i is less than k
    '''

    queue = collections.deque()
    sum_ = 0

    for i in range(n):
        queue.append(array[i])
        sum_ += array[i]

        if i < k-1:
            continue

        sum_ -= queue.popleft()
        if sum_%p >= k:
            return sum_%p

    return -1

def main():

    n, k, p = map(int, raw_input().strip().split())
    array = map(int, raw_input().strip().split())

    print(pre_processing(n, k, p, array))

if __name__ == '__main__':
    main()
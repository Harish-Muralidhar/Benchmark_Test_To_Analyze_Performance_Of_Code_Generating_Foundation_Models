'''

Explanation
Harry first grabs the book with 9 exercises. Then he grabs the book with 6 exercises. Then he grabs the book with 8 exercises.
Now the pile is:

english (remaining exercises: 9)
mathematics (remaining exercises: 6)
geography (remaining exercises: 8)

He wants to do a book exercise, so he removes the book with 6 exercises. He must remove english and geography to pick the book. The number of books he must remove is 2.

Then Harry grabs the book with 3 exercises. Then he wants to do a book exercise. The book with the minimum number of remaining exercises is graphics, so he removes none.



'''


import sys
import heapq

def calculate_minimum_removal(string_input):
    if string_input[0] == -1:
        minimum_removal = 0
        heap = []
        while heap:
            minimum_removal += 1
            heapq.heappop(heap)
        return minimum_removal
    else:
        heapq.heappush(heap, string_input)

if __name__ == '__main__':
    heap = []
    size = int(sys.stdin.readline().rstrip())
    for _ in range(size):
        string_input = list(sys.stdin.readline().strip().split())
        string_input[0] = int(string_input[0])
        print(calculate_minimum_removal(string_input))
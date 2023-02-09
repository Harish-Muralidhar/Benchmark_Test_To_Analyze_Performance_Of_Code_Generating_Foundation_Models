'''

Explanation

Initially, the pile is empty.
Harry grabs the book with 9 remaining exercises. The pile becomes:
english
Harry grabs the book with 6 remaining exercises. The pile becomes:
mathematics
english
Harry grabs the book with 8 remaining exercises. The pile becomes:
geography
mathematics
english
Harry wants to do a book exercise. He removes the book with the minimum number of remaining exercises, which is mathematics. The pile becomes:
geography
english
Harry grabs the book with 3 remaining exercises. The pile becomes:
graphics
geography
english
Harry wants to do a book exercise. He removes the book with the minimum number of remaining exercises, which is graphics. The pile becomes:
geography
english

'''

import heapq

def main():
    n = int(input())
    heap = []
    for i in range(n):
        line = input().split()
        if line[0] == '-1':
            print(len(heap), heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (int(line[0]), line[1]))

if __name__ == '__main__':
    main()
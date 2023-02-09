'''

Solution:
'''

import math

def main():
    t = int(input())
    for i in range(t):
        n,m = map(int, input().split())
        arr = []
        for j in range(n):
            arr.append(list(map(int, input().split())))
        arr.sort(key=lambda x:x[0]*x[1], reverse=True)
        if m == 0:
            print(arr[0][0]*arr[0][1])
        else:
            if n == m:
                print(0)
            else:
                max_area = 0
                for j in range(m, n):
                    max_area = max(max_area, arr[j][0]*arr[j][1])
                print(max_area)

if __name__ == '__main__':
    main()
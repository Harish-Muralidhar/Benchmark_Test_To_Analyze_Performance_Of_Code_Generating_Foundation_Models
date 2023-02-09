'''


'''

#Program

import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n,m = map(int,sys.stdin.readline().split())
        arr = list(map(int,sys.stdin.readline().split()))
        count = 0
        for i in range(n):
            for j in range(i,n):
                if arr[i:j+1].count(128) == 0:
                    count += 1
        print(count)

if __name__ == "__main__":
    main()
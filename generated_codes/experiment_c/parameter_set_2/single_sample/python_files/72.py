'''


'''

import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        l, r, n = map(int, sys.stdin.readline().split())
        count = 0
        for j in range(l, r+1):
            if j%2 == 0:
                count += 1
                if count == n:
                    print(j, "."*j)
                    break
        if count != n:
            print(-1)

if __name__ == "__main__":
    main()
'''

'''

import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        n = int(line[0])
        x = int(line[1])
        line = sys.stdin.readline().strip().split()
        total = 0
        for j in range(n):
            total += int(line[j])
        if total % x == 0:
            print(total // x)
        else:
            print(-1)

if __name__ == '__main__':
    main()
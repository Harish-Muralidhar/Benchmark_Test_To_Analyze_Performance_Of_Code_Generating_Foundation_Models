"""

"""

import sys

def main():
    test_cases = int(sys.stdin.readline().strip())
    for _ in range(test_cases):
        n = int(sys.stdin.readline().strip())
        mem = list(map(int, sys.stdin.readline().strip().split()))
        mem_allocated = 0
        for i in range(n):
            if i == 0:
                mem_allocated += mem[i]
            else:
                if mem[i] > mem[i-1]:
                    mem_allocated += (mem[i] - mem[i-1])
        print(mem_allocated)

if __name__ == '__main__':
    main()
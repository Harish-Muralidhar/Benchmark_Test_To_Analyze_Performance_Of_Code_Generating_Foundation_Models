'''

'''

import sys

def how_it_happened(n, m, a, steps):
    for step in steps:
        s = 0
        for i in range(step - 1):
            s += int(a[i]) - int(a[step - 1])
        print(s)

if __name__ == '__main__':
    n, m = sys.stdin.readline().strip().split()
    n = int(n)
    m = int(m)
    a = sys.stdin.readline().strip()
    a = list(a)
    steps = []
    for i in range(m):
        x = int(sys.stdin.readline().strip())
        steps.append(x)
    how_it_happened(n, m, a, steps)
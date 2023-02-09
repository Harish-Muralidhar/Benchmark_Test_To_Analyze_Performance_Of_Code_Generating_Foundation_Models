"""




"""

from collections import defaultdict
from collections import deque

from sys import stdin

def main():
    for _ in xrange(int(stdin.readline())):
        l = stdin.readline().strip()
        l = deque(l)
        c = 0
        m = 0

        while l:
            a = l.popleft()
            if a == '.':
                c += 1
            else:
                m = max(m, c)
                c = 0
        print m

if __name__ == '__main__':
    main()
'''


'''

import sys

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        s = sys.stdin.readline().strip()
        s = s.replace('#', '1')
        s = s.replace('.', '0')
        s = int(s, 2)
        print(bin(s).count('1') - 1)

if __name__ == '__main__':
    main()
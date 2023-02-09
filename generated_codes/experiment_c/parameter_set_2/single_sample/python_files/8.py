"""

"""

# Write your code here
import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')

if __name__ == '__main__':
    main()
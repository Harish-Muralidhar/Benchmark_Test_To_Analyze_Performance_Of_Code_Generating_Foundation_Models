'''

'''
import sys

def main():
    total_cases = int(sys.stdin.readline())
    for _ in range(total_cases):
        num = sorted([int(i) for i in sys.stdin.readline().strip().split()])
        print(num[1])

if __name__ == '__main__':
    main()
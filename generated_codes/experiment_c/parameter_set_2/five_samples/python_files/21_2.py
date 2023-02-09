'''

'''

# Write your code here
import sys

def main():
    test_cases = int(sys.stdin.readline())
    for i in range(test_cases):
        a, b = map(int, sys.stdin.readline().split())
        print(a % b)

if __name__ == '__main__':
    main()
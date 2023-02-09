'''


'''



import sys

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0
        for i in range(1, n-1):
            if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()
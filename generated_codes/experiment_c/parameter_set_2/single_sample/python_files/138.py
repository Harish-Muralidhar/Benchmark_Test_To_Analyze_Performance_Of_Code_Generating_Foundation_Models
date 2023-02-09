"""


"""



import sys

def main():
    testcases = int(sys.stdin.readline())
    for i in range(testcases):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        count = 0
        for i in range(1, n-1):
            if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                count += 1
        print(count)

if __name__ == "__main__":
    main()
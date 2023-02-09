

A:

<code>#!usr/bin/python
import sys

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, sys.stdin.readline().split()))
        if A[0] != A[-1]:
            print(N)
            continue
        for j in range(N-1):
            if A[j] != A[j+1]:
                print(N-j-1)
                break

if __name__ == '__main__':
    main()
</code>

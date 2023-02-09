"""

Solution:

"""

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        arr = sorted(arr)
        a = []
        for i in range(n):
            a.append(arr[i])
            a.append(arr[i])
        a = sorted(a)
        print(*a)
        
main()
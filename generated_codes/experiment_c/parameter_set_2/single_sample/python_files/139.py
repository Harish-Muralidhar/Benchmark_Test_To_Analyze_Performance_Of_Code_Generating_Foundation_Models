'''

'''

def main():
    test_cases = int(input())
    for i in range(test_cases):
        n,x = map(int,input().split())
        arr = list(map(int,input().split()))
        arr.sort(reverse=True)
        total = 0
        for j in range(n):
            total += arr[j]
            if total >= x*(j+1):
                print(j+1)
                break
            if j == n-1:
                print(-1)

if __name__ == '__main__':
    main()
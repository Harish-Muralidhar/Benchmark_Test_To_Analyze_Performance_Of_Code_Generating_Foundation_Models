'''

'''

def main():
    t = int(input())
    while t > 0:
        n,k = map(int,input().split())
        if k == 0:
            print(*range(1,n+1))
        elif k == n:
            print(-1)
        else:
            for i in range(1,n+1):
                if i <= k:
                    print(i+k,end=" ")
                else:
                    print(i-k,end=" ")
            print()
        t -= 1

if __name__ == '__main__':
    main()
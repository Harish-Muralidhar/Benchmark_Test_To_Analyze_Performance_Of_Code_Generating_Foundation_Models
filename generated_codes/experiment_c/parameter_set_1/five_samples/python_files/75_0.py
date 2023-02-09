'''

'''


def main():
    t = int(input())
    while(t>0):
        x,k = map(int,input().split())
        a = map(int,input().split())
        if sum(a)%(x-1) == 0:
            print("YES")
        else:
            print("NO")
        t-=1

if __name__ == '__main__':
    main()
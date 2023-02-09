'''

'''

def main():
    t = int(input())
    while(t>0):
        n,x = map(int,input().split())
        a = list(map(int,input().split()))
        a.sort()
        s = 0
        for i in a:
            s += i
        if(s%x == 0):
            print(s//x)
        else:
            print(-1)
        t -= 1

if __name__ == '__main__':
    main()
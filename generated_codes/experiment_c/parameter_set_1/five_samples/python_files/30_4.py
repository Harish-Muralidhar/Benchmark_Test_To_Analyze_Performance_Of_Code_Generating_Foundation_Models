'''

'''

def main():
    t = int(input())
    while t > 0:
        a,b,c = input().split()
        a,b,c = int(a), int(b), int(c)
        if (a+b+c == 180):
            print('YES')
        else:
            print('NO')
        t -= 1

if __name__ == '__main__':
    main()
'''

Explanation

In the first example, the first system protects houses 1 through 4, the second system protects houses 3 through 5, and the third system protects houses 6 through 7.

In the second example, the first system protects houses 1 through 4, the second system protects houses 2 through 5, and the third system protects houses 6 through 7.

In the third example, the first system protects houses 1 through 4, the second system protects houses 2 through 5, and the third system protects houses 6 through 7.

In the fourth example, the first system protects houses 1 through 4, the second system protects houses 2 through 5, and the third system protects houses 6 through 7.

In the fifth example, the first system protects houses 1 through 4, the second system protects houses 2 through 5, and the third system protects houses 6 through 7.

'''

import sys

def main():
    n,m=map(int,sys.stdin.readline().split())
    l=[]
    for i in range(m):
        a=sys.stdin.readline().split()
        if a[0]=='P':
            l.append([int(a[1]),int(a[2])])
        elif a[0]=='M':
            l[int(a[1])-1][0]+=int(a[2])
            l[int(a[1])-1][1]+=int(a[2])
        elif a[0]=='B':
            c=0
            for j in range(len(l)):
                if l[j][0]<=int(a[1])<=l[j][1]:
                    c+=1
            print(c)

if __name__=='__main__':
    main()
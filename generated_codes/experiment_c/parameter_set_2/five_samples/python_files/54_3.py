'''

'''

# Write your code here

def find_array(n,e,o):
    if e+o!=n*(n+1)/2:
        print(-1)
    else:
        if e%2==0:
            e=e/2
            o=o/2
            for i in range(n):
                if i<e:
                    print(2,end=" ")
                else:
                    print(1,end=" ")
        else:
            e=(e-1)/2
            o=(o+1)/2
            for i in range(n):
                if i<e:
                    print(2,end=" ")
                elif i==e:
                    print(3,end=" ")
                else:
                    print(1,end=" ")

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        e,o=map(int,input().split())
        find_array(n,e,o)
        print()
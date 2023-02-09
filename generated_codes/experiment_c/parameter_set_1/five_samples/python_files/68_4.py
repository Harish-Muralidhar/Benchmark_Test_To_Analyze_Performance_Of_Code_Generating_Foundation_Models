'''


'''

# Write your code here
testCases=int(input())
for case in range(testCases):
    n,q=map(int,input().split())
    cards=[int(x) for x in input().split()]
    for query in range(q):
        m=int(input())
        s=0
        for i in cards:
            if (i>0):
                s+=i
            else:
                s-=i
        while s>m:
            s=2*m-s
        print(s+1)
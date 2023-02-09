"""

Test 2 : Chef will make two moves: pick up the first two elements (4 and 2), remove the larger one (4), incurring a cost equal to the smaller one (2). Then, pick up the last two remaining elements (2 and 5), remove the larger one (5), incurring a cost equal to the smaller one (2). 


"""

def fun(A):
    A.sort()
    return sum(A[::2])
for i in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    print(fun(A))
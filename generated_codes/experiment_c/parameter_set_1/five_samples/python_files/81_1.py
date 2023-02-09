"""



Test case 1

In this case, Jack and Jill want to visit the locations in the same order so the output placement should minimize dS(P)=dT(P). Since Jack and Jill have a different preference of items, we cannot keep both of them happy at all times. The placement ABA will minimize the maximum difference of dS(P) and dT(P).


Test case 2

In this test case, Jack and Jill want to visit the locations in different orders so the output placement should minimize the maximum of dS(P) and dT(P). The placement AABB will minimize the maximum difference between dS(P) and dT(P).

Limits

    All permutations will be valid and distinct.

    The locations will be visited in the order specified by the permutations.

Sample Input

2
3
1 0 2
2 1 0
4
0 2 1 3
1 2 3 0

Sample Output

ABA
AABB

"""

#Solution 1
from collections import defaultdict
def get_order(jacks_order,jills_order):
    d=defaultdict(lambda:0)
    for i in range(len(jacks_order)):
        d[jacks_order[i]]+=1
        d[jills_order[i]]-=1
    print d
    max_val=max(d.values())
    min_val=min(d.values())
    diff=max_val-min_val
    return diff

def get_order_of_objects(jacks_order,jills_order):
    d2=defaultdict(lambda:'A')
    ans=''
    for i in range(len(jacks_order)):
        if d2[jacks_order[i]]=='A':
            d2[jacks_order[i]]='B'
            ans+='A'
        else:
            d2[jacks_order[i]]='A'
            ans+='B'
    return ans

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    jacks_order = map(int, raw_input().strip().split(' '))
    jills_order = map(int, raw_input().strip().split(' '))
    #print jacks_order,jills_order
    print get_order_of_objects(jacks_order,jills_order)
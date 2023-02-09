'''

Explanation

Test case 1: a[1] is at distance 1 from its correct position, a[2] is at distance 1 from its correct position, and a[3] is at distance 0 from its correct position. Since the maximum distance is 1, the sequence is almost sorted.

Test case 2: a[5] is at distance 2 from its correct position, a[4] is at distance 1 from its correct position, and a[3] is at distance 1 from its correct position. Since the maximum distance is 2, the sequence is not almost sorted.
 
 
 

Solution:

def almostSorted(a, n):
    sorted_a = sorted(a)
    
    if sorted_a == a:
        return "YES"
    else:
        return "NO"
    
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(almostSorted(a, n))
    
    
    
    
'''
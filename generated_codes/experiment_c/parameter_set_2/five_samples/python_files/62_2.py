"""

Explanation
Query 0: The minimum integer in the range [2, 5] is 2.
Query 1: After applying the assignment A[i] = A[i] & 6, the array becomes [1, 4, 2, 2, 4].
Query 2: The minimum integer in the range [2, 2] is 4.
Query 3: After applying the assignment A[i] = A[i] & 3, the array becomes [1, 2, 2, 2, 4].
Query 4: The minimum integer in the range [1, 3] is 0.

"""

# Write your code here
from math import log2,ceil

class SegmentTree:
    def __init__(self,arr):
        self.arr = arr
        self.n = len(arr)
        self.st = [0]*(4*self.n)
        self.build(0,0,self.n-1)
        
    def build(self,si,ss,se):
        if ss == se:
            self.st[si] = self.arr[ss]
            return
        mid = (ss+se)//2
        self.build(2*si+1,ss,mid)
        self.build(2*si+2,mid+1,se)
        self.st[si] = min(self.st[2*si+1],self.st[2*si+2])
        
    def update(self,si,ss,se,l,r,x):
        if ss > se or ss > r or se < l:
            return
        if ss == se:
            self.st[si] = self.st[si] & x
            return
        mid = (ss+se)//2
        self.update(2*si+1,ss,mid,l,r,x)
        self.update(2*si+2,mid+1,se,l,r,x)
        self.st[si] = min(self.st[2*si+1],self.st[2*si+2])
        
    def query(self,si,ss,se,l
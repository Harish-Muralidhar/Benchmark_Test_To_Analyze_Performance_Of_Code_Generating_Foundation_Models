'''

SOLUTION:
'''

# cook your dish here
import math
import itertools
def main():
    t=int(input())
    while t!=0:
        t=t-1
        n=int(input())
        if n==1:
            print(1)
        else:
            res=math.ceil(math.log2(n))
            print(res)
    return
main()
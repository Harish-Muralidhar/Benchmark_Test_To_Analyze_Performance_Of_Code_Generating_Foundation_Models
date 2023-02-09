'''
'''

# cook your dish here
import sys

def no_of_pairs(a):
    l = []
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                l.append((a[i],a[j]))
    return l

if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        a = list(map(int,sys.stdin.readline().strip().split()))
        print(len(no_of_pairs(a)))
        t -= 1
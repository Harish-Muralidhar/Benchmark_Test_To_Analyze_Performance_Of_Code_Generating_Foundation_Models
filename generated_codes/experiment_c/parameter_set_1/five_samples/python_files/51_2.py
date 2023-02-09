"""



Explanation of two sample cases
In first case, minimum total bonus to be divided among the employees is 460$. Bonus distribution will be 140, 120, 100 and 100, where first number refers to the first employee, and so on.
In second case, it’s not possible to give minimum bonus to all the employees, so output is "cmtt-10x-x-109">Inconsistent "cmtt-10x-x-109">analysis.

@author: narendra
"""

def min_bonus(e,m,l):
    total_bonus = 0
    bonus = {}
    for i in range(1,e+1):
        bonus[i] = l
    for i in range(1,m+1):
        e1,e2,inc = map(int,raw_input().split())
        if bonus[e1] < bonus[e2]+inc:
            bonus[e1] = bonus[e2]+inc
    for i in range(1,e+1):
        total_bonus += bonus[i]
    for i in range(1,e+1):
        print bonus[i],
    print
    print total_bonus
    
def main():
    t = int(raw_input())
    for i in range(t):
        e,m,l = map(int,raw_input().split())
        min_bonus(e,m,l)
    return
main()
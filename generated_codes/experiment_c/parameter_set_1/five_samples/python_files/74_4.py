"""

Explanation

In the first example there are two progressions with length 3: (2,4,6) and (3,5,7). They are lexicographically ordered as (2,4,6) < (3,5,7). Hence, the first two terms of the first such progression are 2 and 4.

In the second example the answer is 0 0 because there is only one such progression.

In the third example there are four progressions with length 4: (5,9,13,17), (5,10,15,20), (6,11,16,21) and (6,12,18,24). They are lexicographically ordered as (5,9,13,17) < (5,10,15,20) < (6,11,16,21) < (6,12,18,24). Hence, the first two terms of the twelfth such progression are 5 and 14.

"""

def lexicographic_ordering(L,R,k,n):
    if n > 0:
        new_list = []
        for x in range(L,R+1):
            for y in range(x,R+1,k):
                new_list.append([x,y])
        return new_list[n-1][0], new_list[n-1][1]
    else:
        return 0,0
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        L,R,k,n = [int(i) for i in input().split()]
        print(len(range(L,R+1,k)),*lexicographic_ordering(L,R,k,n))
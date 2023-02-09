'''
Input:
1
3
1
3
4
Output:
4
Input:
1
7
1
2
2
3
3
4
4
Output:
5

Explanation

In the first example the array that is left is [1,2,1]. The element 2 is the odd one out.
'''
import collections
for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    d = collections.Counter(l)
    print(d.most_common()[-1][0])
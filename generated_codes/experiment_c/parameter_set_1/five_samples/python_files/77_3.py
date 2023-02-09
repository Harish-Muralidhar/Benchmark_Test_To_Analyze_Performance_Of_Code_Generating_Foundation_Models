"""
 

Example 3


Input:
7 5
D....
.....
.....
DD..D
.....
.....
@....

Output:
3


 

Example 4


Input:
7 5
D....
.....
D....
DD..D
.....
.....
@....

Output:
4


 

Example 5


Input:
7 5
D....
.....
DDD..
DD..D
.....
.....
@....

Output:
1

 

Example 6


Input:
7 5
D....
.....
DDD..
DD..D
.....
.....
@..DD

Output:
5


 

Example 7


Input:
7 5
D....
.....
.....
.....
@DDD.
.....
.DDDD

Output:
1


 

Example 8


Input:
7 5
D....
.....
..D..
.....
@DDD.
.....
.DDDD

Output:
2



Example 9


Input:
7 5
D....
.....
..D..
.....
@.DD.
.....
.DDDD

Output:
3


 

Example 10


Input:
7 5
D....
.....
..D..
.....
@DDD.
.....
.DD.D

Output:
4

"""
def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def find_spoon(monsters, spoon, chef):
    min_dist = 9999999999999
    for monster in monsters:
        min_dist = min(min_dist, dist(monster, spoon) - dist(chef, monster))
    return min_dist

n, m = map(int, input().split())
monsters = []
spoon = None
chef = None
for i in range(n):
    row = list(input().strip())
    for j in range(m):
        if row[j] == 'D':
            monsters.append((i, j))
        elif row[j] == '$':
            spoon = (i, j)
        elif row[j] == '@':
            chef = (i, j)
print(find_spoon(monsters, spoon, chef))
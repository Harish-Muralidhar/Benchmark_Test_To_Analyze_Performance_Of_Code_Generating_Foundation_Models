'''

Example 3


Input:
7 5
....$
.....
.....
D...D
.....
.....
@DDDD

Output:
1

'''

import numpy as np

def find_distance(n,m,list1):
    #print(list1)
    list1 = np.array(list1)
    #print(list1)
    chef_x = np.where(list1=='@')[0][0]
    chef_y = np.where(list1=='@')[1][0]
    spoon_x = np.where(list1=='$')[0][0]
    spoon_y = np.where(list1=='$')[1][0]
    #print(chef_x,chef_y,spoon_x,spoon_y)
    if np.where(list1=='D')[0].size==0:
        return 0
    else:
        monster_x = np.where(list1=='D')[0]
        monster_y = np.where(list1=='D')[1]
        #print(monster_x,monster_y)
        dist = []
        for i in range(len(monster_x)):
            dist.append(abs(chef_x-monster_x[i])+abs(chef_y-monster_y[i]))
        #print(dist)
        return min(dist)

if __name__=='__main__':
    n,m = map(int,input().split())
    list1 = []
    for i in range(n):
        list1.append(list(input()))
    print(find_distance(n,m,list1))
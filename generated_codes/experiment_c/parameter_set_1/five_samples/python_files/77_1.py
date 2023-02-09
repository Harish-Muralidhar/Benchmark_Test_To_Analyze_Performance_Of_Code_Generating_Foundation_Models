'''

Example 3


Input:
7 5
@....
.....
.....
DDDDD
.....
.....
....$

Output:
5


Example 4


Input:
5 5
D....
.....
..$..
.....
@....

Output:
2



Example 5


Input:
5 5
@....
.....
..$..
.....
D....

Output:
4



Example 6


Input:
5 5
.....
@....
..$..
.....
D....

Output:
2



Example 7


Input:
9 9
..D....$.
..........
.D....D...
..........
..........
.D........
..D.......
.........@
..........

Output:
2



Example 8


Input:
9 9
..........
..........
..........
...@......
..........
..........
..........
..........
..........

Output:
0

'''

def distance_of_chef_from_monster(matrix):
    #find chef
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '@':
                chef_pos = (i,j)
                break
    
    #find monster
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'D':
                monster_pos = (i,j)
                break
    
    #find spoon
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '$':
                spoon_pos = (i,j)
                break
    
    #print(chef_pos)
    #print(monster_pos)
    #print(spoon_pos)
    
    #find distance of monster from spoon
    monster_spoon = [0]
    def find_distance_from_spoon(matrix,chef_pos,spoon_pos):
        #print('spoon')
        #print(chef_pos)
        #print(spoon_pos)
        if chef_pos == spoon_pos:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '@' or matrix[i][j] == 'D':
                    continue
                matrix[i][j] = '@'
                chef_pos = (i,j)
                monster_spoon.append(find_distance_from_spoon(matrix,chef_pos,spoon_pos))
                matrix[i][j] = '.'
        return min(monster_spoon)
    
    #print(monster_spoon)
    monster_spoon_distance = find_distance_from_spoon(matrix,chef_pos,spoon_pos)
    #print(monster_spoon_distance)
    
    #find distance of chef from monster
    chef_monster = [0]
    def find_distance_from_monster(matrix,chef_pos,monster_pos):
        #print('monster')
        #print(chef_pos)
        #print(monster_pos)
        if chef_pos == monster_pos:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '@' or matrix[i][j] == 'D':
                    continue
                matrix[i][j] = '@'
                chef_pos = (i,j)
                chef_monster.append(find_distance_from_monster(matrix,chef_pos,monster_pos))
                matrix[i][j] = '.'
        return min(chef_monster)
    
    #print(chef_monster)
    chef_monster_distance = find_distance_from_monster(matrix,chef_pos,monster_pos)
    #print(chef_monster_distance)
    
    if chef_monster_distance <= monster_spoon_distance:
        return 0
    else:
        return chef_monster_distance-monster_spoon_distance

matrix = [
['.','.','.','.','$'],
['.','.','.','.','.'],
['.','.','.','.','.'],
['D','.','.','.','D'],
['.','.','.','.','.'],
['.','.','.','.','.'],
['@','.','.','.','.']
]

print(distance_of_chef_from_monster(matrix))
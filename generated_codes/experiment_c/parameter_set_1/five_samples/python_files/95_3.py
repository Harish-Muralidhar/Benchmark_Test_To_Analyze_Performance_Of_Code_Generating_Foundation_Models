'''

Example 3
Input:
2 2
00
00

Output:
5

Explanation
In the second test case, there are following sub-rectangle

2 X 3 : (1, 2) - (2, 4)
2 X 3 : (2, 2) - (3, 4)
3 X 2 : (1, 1) - (3, 2)
3 X 2 : (1, 2) - (3, 3)
3 X 2 : (1, 3) - (3, 4)
2 X 3 : (2, 1) - (3, 3)
2 X 3 : (2, 2) - (3, 4)
2 X 3 : (2, 3) - (3, 5)
2 X 3 : (2, 2) - (3, 4)
2 X 3 : (2, 1) - (3, 3)
3 X 2 : (1, 2) - (3, 3)
3 X 2 : (1, 1) - (3, 2)
3 X 2 : (1, 3) - (3, 4)

Answer: 26

'''

def function(N,M,cake):
    odd_count = 0
    even_count = 0
    for i in range(N):
        for j in range(M):
            if cake[i][j] == 1:
                odd_count +=1
            else:
                even_count +=1
    return odd_count * even_count

N,M = map(int,input().split())
cake = []
for i in range(N):
    cake.append(list(map(int,input())))
print(function(N,M,cake))
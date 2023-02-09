'''
 

Explanation
In the first example, all sub-rectangles contain even number of currants.

In the second example, the sub-rectangles with even number of currants are :
1) 1 row and 2 columns
2) 1 row and 4 columns
3) 2 rows and 1 column
4) 2 rows and 2 columns
5) 2 rows and 4 columns
6) 3 rows and 1 column
7) 3 rows and 2 columns
8) 3 rows and 4 columns

There are total 8 different sub-rectangles, each of them contains even number of currants.

'''

# Write your code here
def evenCake(cake):
    evenCakeCount = 0
    cache = {}
    evenRowCount = 0
    oddRowCount = 0
    evenColumnCount = 0
    oddColumnCount = 0
    n = len(cake)
    m = len(cake[0])
    for i in range(n):
        for j in range(m):
            if cake[i][j]==1:
                if i not in cache:
                    cache[i]={}
                if j not in cache[i]:
                    cache[i][j]=1
                else:
                    cache[i][j]+=1
    for i in range(n):
        for j in range(m):
            if i in cache and j in cache[i]:
                if cache[i][j]%2==0:
                    evenCakeCount+=1
                    evenRowCount+=1
                    evenColumnCount+=1
                else:
                    oddRowCount+=1
                    oddColumnCount+=1
            else:
                evenColumnCount+=1
                evenRowCount+=1
        evenCakeCount+=evenRowCount*evenColumnCount
        evenCakeCount+=oddRowCount*oddColumnCount
        evenRowCount = 0
        oddRowCount = 0
        evenColumnCount = 0
        oddColumnCount = 0
    return evenCakeCount

print(evenCake([[1,0],[0,1]]))
print(evenCake([[1,0,1,0],[0,1,0,1],[1,1,1,0]]))
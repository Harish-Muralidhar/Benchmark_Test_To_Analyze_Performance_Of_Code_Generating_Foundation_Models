/*


Constraints

1 ≤ t ≤ 1000

-2100000000 ≤ Y ≤ 2100000000

-2100000000 ≤ X1 ≤ X2 ≤ 2100000000

X2 - X1 ≤ 109

SAMPLE INPUT 
1
2 -2 1
SAMPLE OUTPUT 
2
Explanation
Example case 1. From the picture, you can see that your cannon can only destroy the guns located at the points (-2, 2) and (-1, 2).

*/

t=int(input())
for i in range(t):
    y,x1,x2=map(int,input().split())
    if x1<0:
        x=x1*-1
        x1=x
        x2=x2+x
    else:
        x2=x2-x1
    print(x2+1)
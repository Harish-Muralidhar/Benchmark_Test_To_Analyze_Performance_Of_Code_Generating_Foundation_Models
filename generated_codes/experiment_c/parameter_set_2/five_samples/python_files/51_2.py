/*


Explanation

In the first case, employee 1 should get at least 140$ more than employee 2, employee 2 should get at least 120$ more than employee 3, and employee 1 should get at least 100$ more than employee 3. So, employee 1 should get at least 140+120=260$ more than employee 3. Also, employee 2 should get at least 120+100=220$ more than employee 4. So, employee 1 should get at least 260+220=480$ more than employee 4. So, the minimum total bonus is at least 480+100=580$. But, if we give 580$ to employee 1, and 100$ to employee 4, we can give 140$ to employee 2, and 120$ to employee 3. So, the minimum total bonus is 460$.

In the second case, employee 1 should get at least 10$ more than employee 2, employee 2 should get at least 10$ more than employee 3, and employee 3 should get at least 10$ more than employee 1. So, the comparisons are inconsistent, and it’s not possible to distribute bonus among them.

*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m,l;
        cin>>n>>m>>l;
        int a[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(i==j)
                {
                    a[i][j]=0;
                }
                else
                {
                    a[i][j]=INT_MAX;
                }
            }
        }
        for(int i=0;i<m;i++)
        {
            int x,y,z;
            cin>>x>>y>>z;
            a[x-1][y-1]=z;
        }
        for(int k=0;k<n;k++)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;
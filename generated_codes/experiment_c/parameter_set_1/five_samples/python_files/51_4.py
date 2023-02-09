/*
*/

#include<iostream>
#include<bits/stdc++.h>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m,l;
        cin>>n>>m>>l;
        vector<vector<int>> dp(n,vector<int>(n,0));
        for(int i=0;i<m;i++)
        {
            int x,y,cost;
            cin>>x>>y>>cost;
            x--;
            y--;
            dp[x][y]=cost;
        }
        int ans = 0;
        for(int k=0;k<n;k++)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(dp[i][k]>0 && dp[k][j]>0 && dp[i][j]<max(dp[i][k],dp[k][j]))
                    {
                        dp[i][j]=max(dp[i][k],dp[k][j]);
                    }
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(dp[i][j]==0)
                {
                    cout<<"Inconsistent analysis"<<endl;
                    goto end;
                }
                else
                {
                    ans+=dp[i][j];
                }
            }
        }
        cout<<ans+n*l<<endl;
        for(int i=0;i<n;i++)
        {
            cout<<l+dp[i][i]<<" ";
        }
        cout<<endl;
        end:
        ;
    }
}
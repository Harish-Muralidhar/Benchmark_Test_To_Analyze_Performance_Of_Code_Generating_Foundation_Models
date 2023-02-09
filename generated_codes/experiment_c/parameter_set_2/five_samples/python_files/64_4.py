/*

*/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000009
#define MAX 100005

ll dp[MAX][4];

ll solve(ll n,ll k)
{
    if(n==0 && k==0)
        return 1;
    if(n<0 || k<0)
        return 0;
    if(dp[n][k]!=-1)
        return dp[n][k];
    ll ans=0;
    for(ll i=0;i<=n;i++)
    {
        ans+=solve(n-i,k-1);
        ans%=mod;
    }
    dp[n][k]=ans;
    return ans;
}

int main()
{
    ll t,n,k;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        memset(dp,-1,sizeof(dp));
        cout<<solve(n,k)<<endl;
    }
    return 0;
}
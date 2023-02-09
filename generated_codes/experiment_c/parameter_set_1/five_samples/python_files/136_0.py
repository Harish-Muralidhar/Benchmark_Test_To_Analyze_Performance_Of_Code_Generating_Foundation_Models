"""

Hint: Use dynamic programming.

"""

#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define mset(a,b) memset(a,b,sizeof(a))

ll dp[1000005];

ll solve(ll n,ll k)
{
	if(dp[n]!=-1)
		return dp[n];
		
	if(n==0)
		return 1;
	if(n==1)
		return k;
		
	ll r=0;
	ll i;
	for(i=1;i<=k;i++)
	{
		r=(r+solve(n-1,k))%mod;
	}
	dp[n]=r;
	return r;
}

int main()
{
	ll t,n,k;
	cin>>t;
	
	mset(dp,-1);
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<solve(n,k)<<endl;
	}
}

"""

"""

#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define mset(a,b) memset(a,b,sizeof(a))

ll dp[1000005];

ll solve(ll n,ll k)
{
	if(dp[n]!=-1)
		return dp[n];
		
	if(n==0)
		return 1;
	if(n==1)
		return k;
		
	ll r=0;
	ll i;
	for(i=1;i<=k;i++)
	{
		r=(r+solve(n-1,k))%mod;
	}
	dp[n]=r;
	return r;
}

int main()
{
	ll t,n,k;
	cin>>t;
	
	mset(dp,-1);
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<solve(n,k)<<endl;
	}
}

"""

"""

#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define mset(a,b) memset(a,b,sizeof(a))

ll dp[1000005];

ll solve(ll n,ll k)
{
	if(dp[n]!=-1)
		return dp[n];
		
	if(n==0)
		return 1;
	if(n==1)
		return k;
		
	ll r=0;
	ll i;
	for(i=1;i<=k;i++)
	{
		r=(r+solve(n-1,k))%mod;
	}
	dp[n]=r;
	return r;
}

int main()
{
	ll t,n,k;
	cin>>t;
	
	mset(dp,-1);
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<solve(n,k)<<endl;
	}
}

"""

"""

#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define mset(a,b) memset(a,b,sizeof(a))

ll dp[1000005];

ll solve(ll n,ll k)
{
	if(dp[n]!=-1)
		return dp[n];
		
	if(n==0)
		return 1;
	if(n==1)
		return k;
		
	ll r=0;
	ll i;
	for(i=1;i<=k;i++)
	{
		r=(r+solve(n-1,k))%mod;
	}
	dp[n]=r;
	return r;
}

int main()
{
	ll t,n,k;
	cin>>t;
	
	mset(dp,-1);
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<solve(n,k)<<endl;
	}
}

"""

"""

#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define mset(a,b) memset(a,b,sizeof(a))

ll dp[1000005];

ll solve(ll n,ll k)
{
	if(dp[n]!=-1)
		return dp[n];
		
	if(n==0)
		return 1;
	if(n==1)
		return k;
		
	ll r=0;
	ll i;
	for(i=1;i<=k;i++)
	{
		r=(r+solve(n-1,k))%mod;
	}
	dp[n]=r;
	return r;
}

int main()
{
	ll t,n,k;
	cin>>t;
	
	mset(dp,-1);
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<solve(n,k)<<endl;
	}
}

"""

"""

#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define mset(a,b) memset(a,b,sizeof(a))

ll dp[1000005];

ll solve(ll n,ll k)
{
	if(dp[n]!=-1)
		return dp[n];
		
	if(n==0)
		return 1;
	if(n==1)
		return k;
		
	ll r=0;
	ll i;
	for(i=1;i<=k;i++)
	{
		r=(r+solve(n-1,k))%mod;
	}
	dp[n]=r;
	return r;
}

int main()
{
	ll t,n,k;
	cin>>t;
	
	mset(dp,-1);
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<solve(n,k)<<endl;
	}
}

"""
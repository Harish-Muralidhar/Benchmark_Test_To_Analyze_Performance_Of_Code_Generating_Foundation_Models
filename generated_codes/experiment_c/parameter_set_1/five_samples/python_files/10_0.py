/*

Examples

Input
5 1
3 4 3 4 3
Output
81

Input
5 2
3 4 3 4 3
Output
12

Input
10 1
1 2 3 4 5 6 7 8 9 10
Output
3628800

*/

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

#define ll long long

int main()
{
	ll n,k;
	cin>>n>>k;
	ll arr[n+1], dp[n+1];
	arr[0] = 1;
	dp[0] = 1;
	for(ll i=1;i<=n;i++)
	{
		cin>>arr[i];
	}

	for(ll i=1;i<=n;i++)
	{
		dp[i] = 0;
		for(ll j=1;j<=k && i-j>=0;j++)
		{
			dp[i] += (dp[i-j]%1000000007)*(arr[i-j]%1000000007);
			dp[i] = dp[i]%1000000007;
		}
	}
	cout<<dp[n]<<endl;
}
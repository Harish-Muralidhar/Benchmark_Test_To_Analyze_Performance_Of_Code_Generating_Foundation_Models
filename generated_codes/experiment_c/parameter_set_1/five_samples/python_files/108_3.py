

#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll t,n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		ll i=0,count=0,pos=1;
		while(n>0)
		{
			count++;
			n=n-pos;
			pos++;
		}
		cout<<count<<endl;
	}
	return 0;
}
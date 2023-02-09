/*

*/

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		long long int x,b,c,i,temp,sum=0;
		scanf("%lld",&x);
		scanf("%lld",&b);
		long long int d[b],r[b];
		for(i=0;i<b;i++)
		{
			scanf("%lld",&d[i]);
			scanf("%lld",&r[i]);
		}
		scanf("%lld",&c);
		long long int p[c],q[c],s[c];
		for(i=0;i<c;i++)
		{
			scanf("%lld",&p[i]);
			scanf("%lld",&q[i]);
			scanf("%lld",&s[i]);
		}
		sort(d,d+b);
		sort(p,p+c);
		for(i=0;i<b;i++)
		{
			if(d[i]==x)
			{
				sum+=r[i];
				break;
			}
			sum+=r[i];
		}
		for(i=0;i<c;i++)
		{
			if(p[i]==x)
			{
				sum+=s[i];
				break;
			}
			sum+=s[i];
		}
		printf("%lld\n",sum);
	}
	return 0;
}
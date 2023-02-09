

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        cin>>n>>q;
        long long int a[n];
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
        }
        while(q--)
        {
            int m;
            cin>>m;
            long long int sum=0;
            long long int ans=0;
            for(int i=0;i<n;i++)
            {
                sum+=a[i];
                if(sum%m==0)
                {
                    ans++;
                }
            }
            cout<<ans<<endl;
        }
    }
    return 0;
}
'''

Explanation

1) There are two systems. The first one protects houses 1 through 4, the second one protects houses 3 through 5.
2) The second system is moved 1 house to the right. So, it protects houses 4 through 6.
3) There are two systems. The first one protects houses 1 through 4, the second one protects houses 4 through 6.



'''



'''
#include <bits/stdc++.h>
#define pb push_back
using namespace std;
int n,m, a[250001];
vector <int> v;
int main()
{
    cin>>n>>m;
    for(int i=0;i<m;i++)
    {
        char ch;
        cin>>ch;
        if(ch=='P')
        {
            int u,v;
            cin>>u>>v;
            a[u]++;
            a[v+1]--;
        }
        else if(ch=='M')
        {
            int i,d;
            cin>>i>>d;
            a[i]+=d;
            a[i+1]-=d;
        }
        else
        {
            int x;
            cin>>x;
            v.pb(x);
        }
    }
    for(int i=1;i<=n;i++)
    {
        a[i]+=a[i-1];
    }
    for(int i=0;i<v.size();i++)
    {
        cout<<a[i]<<endl;
    }
    return 0;
}


'''
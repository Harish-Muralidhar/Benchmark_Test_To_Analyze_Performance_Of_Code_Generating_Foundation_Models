/*

*/

#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int>a(n);
        for(auto &i:a)
            cin>>i;
        vector<int>b(n);
        for(auto &i:b)
            cin>>i;
        vector<int>index(n+1,0);
        for(int i=0;i<n;i++)
        {
            index[a[i]]=i;
        }
        vector<int>temp(n+1,0);
        int lis=1;
        int lcs=0;
        temp[0]=index[b[0]];
        for(int i=1;i<n;i++)
        {
            if(index[b[i]]<temp[0])
            {
                temp[0]=index[b[i]];
            }
            else if(index[b[i]]>temp[lis-1])
            {
                temp[lis]=index[b[i]];
                lis++;
            }
            else
            {
                int *lb=lower_bound(temp.begin(),temp.begin()+lis,index[b[i]]);
                *lb=index[b[i]];
            }
        }
        cout<<lis<<endl;
    }
    return 0;
}
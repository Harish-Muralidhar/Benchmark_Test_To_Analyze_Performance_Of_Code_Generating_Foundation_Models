/*


*/



#include<bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define loop(k) for(i=0;i<k;++i)
#define loop2(k) for(j=0;j<k;++j)
#define mod 1000000007
using namespace std;
int main()
{
    std::ios_base::sync_with_stdio(false);cin.tie(NULL);
    ll t=1,i=0,j=0,k=0;
    //cin>>t;
    while(t--){
        ll n;
        cin>>n;
        ll a[n],d[n];
        loop(n)cin>>a[i];
        d[0]=1;
        d[1]=5;
        d[2]=5*5+5;
        d[3]=5*5*5+5*5+5+5*5;
        loop(n-3){
            d[i+4]=d[i+3]+5*d[i+2]+5*5*d[i+1]+5*5*5*d[i];
        }
        cout<<d[n]<<"\n";
    }
    return 0;
}
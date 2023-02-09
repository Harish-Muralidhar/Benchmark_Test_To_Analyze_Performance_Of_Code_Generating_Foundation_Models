'''
 

*/


'''
#include<bits/stdc++.h>
using namespace std;
#define ll long long

const int mod=1000000007;

int main(){
    ll t;
    cin>>t;
    while(t--){
        ll n,k,ans=1;
        cin>>n>>k;
        while(n--){
            ans=(ans*k)%mod;
            k--;
        }
        cout<<ans<<endl;
    }
}
'''
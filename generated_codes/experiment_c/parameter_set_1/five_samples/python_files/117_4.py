/*

Explanation
In the first test case, Captain selected position 1 in first round. So the numbers are assigned as follows.
[1, 0, 1, 2]

In the second test case, Captain selected position 2 in first round and position 3 in second round. So the numbers are assigned as follows.

Round 1 : [2, 1, 0, 1, 2, 3]
Round 2 : [3, 2, 1, 1, 2, 3]

*/


#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ff first 
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define in(x) insert(x)
#define ffor(i,a,b) for(int i=a;i<b;i++)
#define bfor(i,a,b) for(int i=a;i>=b;i--)
#define PI 3.14159265358979323846
#define SP(x) setprecision(x)
#define reflex ios_base::sync_with_stdio(false);cin.tie(NULL)

int main(){
    reflex;
    int t;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        int a[n];
        ffor(i,0,n)a[i]=i;
        while(m--){
            int x;
            cin>>x;
            ffor(i,0,x+1){
                swap(a[i],a[x-i]);
            }
        }
        ffor(i,0,n)cout<<a[i]<<" ";
        cout<<endl;
    }
}
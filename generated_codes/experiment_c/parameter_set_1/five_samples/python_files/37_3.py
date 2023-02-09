/*



*/


#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n,m,k;
	    cin>>n>>m>>k;
	    int min1= min(n,m);
	    int max1= max(n,m);
	    if(max1-min1<=k){
	        cout<<"0";
	    }
	    
	    else{
	        cout<<max1-min1-k;
	    }
	    cout<<endl;
	}
	return 0;
}
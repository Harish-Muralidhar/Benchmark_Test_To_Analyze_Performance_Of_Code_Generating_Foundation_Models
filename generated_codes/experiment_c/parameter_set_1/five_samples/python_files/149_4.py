/*

*/

#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
	ll t,n,i,sum;
	cin>>t;
	while(t--){
		sum = 0;
		cin>>n;
		ll a[n];
		for(i=0;i<n;i++)
		cin>>a[i];
		for(i=0;i<n-1;i++){
			if(a[i+1]>a[i])
			sum += a[i+1] - a[i];
		}
		cout<<sum<<endl;
		
	}
}
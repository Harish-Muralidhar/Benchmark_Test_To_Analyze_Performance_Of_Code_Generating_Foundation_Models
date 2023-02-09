/*

*/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    int a[n];
	    int b[n];
	    for(int i=0;i<n;i++)
	        cin>>a[i];
	    for(int i=0;i<n;i++)
	        cin>>b[i];
	    map<int,int> mp;
	    for(int i=0;i<n;i++)
	        mp[a[i]]++;
	    int ans=0;
	    for(int i=0;i<n;i++){
	        if(mp[b[i]]){
	            mp[b[i]]--;
	            ans++;
	        }
	    }
	    cout<<ans<<'\n';
	}
	return 0;
}
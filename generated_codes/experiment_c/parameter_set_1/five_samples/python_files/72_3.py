/*

*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	//code
	int t;
	cin >> t;
	while(t--){
	    long long l,r,n,i,j,ans;
	    cin >> l >> r >> n;
	    n++;
	    long long dp[n];
	    dp[0] = 1;
	    ans = -1;
	    for(i=1;i<n;i++){
	        dp[i] = 0;
	        for(j=0;j<i;j++){
	            dp[i] += dp[j];
	            if(dp[i] > r)
	                break;
	        }
	        if(dp[i] > r)
	            break;
	        if(dp[i] >= l && dp[i] <= r){
	            ans = dp[i];
	            n = i;
	        }
	    }
	    if(ans != -1){
	        cout << ans << " ";
	        for(i=0;i<n;i++){
	            if(i%2 == 0)
	                cout << ".";
	            else
	                cout << "#";
	        }
	        cout << endl;
	    }
	    else
	        cout << ans << endl;
	}
	return 0;
}
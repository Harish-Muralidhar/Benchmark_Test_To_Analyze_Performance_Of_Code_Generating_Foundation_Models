
A:

The question is asking to find the number of subset, the sum of which is divisible by a number m. The sum can be calculated by finding the modulo of the sum of the input numbers with respect to m. For example, for the input
<blockquote>
<p>5 2 1 2 3 4 5 5 15</p>
</blockquote>
<code>Sum of all numbers = 15
Modulo of sum with respect to 5 = 0
</code>
Now, we need to find the number of subset whose sum is divisible by m. This can be done by a dynamic programming solution. The time complexity will be O(N2) and space complexity will be O(N). 
<code>for (i = 1 to n)
   for (j = 1 to m)
       dp[i][j] = dp[i-1][j] + dp[i-1][(j-arr[i]+m)%m]
return dp[n][0];
</code>
Here is the code
<code>#include&lt;bits/stdc++.h&gt;

#define MOD 1000000009

using namespace std;

int main(){
  int t, n, q, m;
  cin&gt;&gt;t;
  while(t--){
    cin&gt;&gt;n&gt;&gt;q;
    int arr[n];
    for(int i=0;i&lt;n;++i){
      cin&gt;&gt;arr[i];
    }
    int dp[n][100];
    while(q--){
      cin&gt;&gt;m;
      memset(dp, 0, sizeof(dp));
      for (int i = 0; i &lt; n; ++i)
	dp[i][0] = 1;

      for (int i = 1; i &lt; n; ++i)
	for (int j = 1; j &lt;= m; ++j)
	  dp[i][j] = dp[i-1][j] + dp[i-1][(j-arr[i]+m)%m];
      cout&lt;&lt;dp[n-1][0]&lt;&lt;endl;
    }
  }
  return 0;
}
</code>
The required answer is the dp[n-1][0] (the number of subset with sum equal to 0 which is divisible by m).

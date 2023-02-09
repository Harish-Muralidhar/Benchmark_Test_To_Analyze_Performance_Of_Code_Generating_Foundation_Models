
Input:
4 5 5Output:
16Explanation:

The 16 and-tuples are (4,0,0,0,0), (3,1,0,0,0), (3,0,1,0,0), (3,0,0,1,0), (3,0,0,0,1), (2,2,0,0,0), (2,1,1,0,0), (2,1,0,1,0), (2,1,0,0,1), (2,0,2,0,0), (2,0,1,1,0), (2,0,1,0,1), (2,0,0,2,0), (2,0,0,1,1), (2,0,0,0,2), (1,1,1,1,0).

Input:
1 1 1Output:
1Explanation:

The only and-tuple is (1,).



#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define F first
#define S second
#define ford(i,n) for(int i = n-1;i>=0;i--)
#define pi pair<int, int>
#define vi vector<int>
#define vpi vector<pi>
#define sort(a) sort(a.begin(), a.end())
#define sort1(a, n) sort(a, a+n)
#define sort2(a, n, m) sort(a, a+n, greater<int>())
#define FAST {ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);}
#define SQ(x) ((x)*(x))
#define MOD(x) ((x)%MOD1)
#define MOD1 999999937
//#define int unsigned long long
#define N 1000001

const int inf = 10000000000000;
const long long INF = 1000000000000000000;

#define K 4
#define maxN 1000000000000

long long dp[K][N];

long long compute(int k, int n) {
    if (n == 0) return 1;

    if (k < 1) return 0;

    if (dp[k][n] != -1) return dp[k][n];

    long long res = 0;
    for (int i=0; i<=n; i++) {
        res += compute(k-1, i);
        res %= MOD1;
    }

    return dp[k][n] = res;
}

int main() {
    FAST
    int t;
    cin >> t;

    memset(dp, -1, sizeof(dp));

    while (t--) {
        int k, n;
        cin >> k >> n;

        cout << compute(k, n) << "\n";
    }
}
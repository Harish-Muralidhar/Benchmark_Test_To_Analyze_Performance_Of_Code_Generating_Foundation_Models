/*

-------


#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
#include <bitset>
#include <set>
#include <map>
#include <stack>
using namespace std;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define EPS (1e-10)
#define INF (1<<30)
#define PI (2*acos(0.0))
#define sf scanf
#define pf printf
#define ab(a) (((a)>0)?(a):-(a))
#define MAX 300
#define MAX1 10000


typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;

int dp[MAX][MAX][MAX1];
int a[MAX][MAX];
int n, m, sx, sy, fx, fy;

int dx[] = {-1, -2, 1, 2, 0, 0, 0, 0};
int dy[] = {0, 0, 0, 0, -1, -2, 1, 2};

void solve()
{
	for(int i = 0; i <= n; i++)
		for(int j = 0; j <= m; j++)
			for(int k = 0; k <= 100; k++)
				dp[i][j][k] = 0;
	dp[sx][sy][a[sx][sy]] = 1;
	for(int k = a[sx][sy]; k >= 0; k--)
	{
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= m; j++)
			{
				if(k >= a[i][j])
				{
					for(int l = 0; l < 8; l++)
					{
						int xx = i + dx[l];
						int yy = j + dy[l];
						if(xx > 0 && xx <= n && yy > 0 && yy <= m)
						{
							dp[i][j][k] += dp[xx][yy][k + 1];
							dp[i][j][k] %= MOD;
						}
					}
				}
			}
		}
	}
	// for(int k = 1; k <= a[sx][sy]; k++)
	// {
	// 	for(int i = 1; i <= n; i++)
	// 	{
	// 		for(int j = 1; j <= m; j++)
	// 		{
	// 			if(k >= a[i][j])
	// 			{
	// 				for(int l = 0; l < 8; l++)
	// 				{
	// 					int xx = i + dx[l];
	// 					int yy = j + dy[l];
	// 					if(xx > 0 && xx <= n && yy > 0 && yy <= m)
	// 					{
	// 						dp[i][j][k] += dp[xx][yy][k + 1];
	// 						dp[i][j][k] %= MOD;
	// 					}
	// 				}
	// 			}
	// 		}
	// 	}
	// }
	int ans = 0;
	for(int k = 1; k <= a[fx][fy]; k++)
		ans = (ans + dp[fx][fy][k]) % MOD;
	cout << ans << endl;
}

int main()
{
	int t;
	cin >> t;
	while(t--)
	{
		cin >> n >> m;
		cin >> sx >> sy;
		cin >> fx >> fy;
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= m; j++)
			{
				cin >> a[i][j];
			}
		}
		solve();
	}
	return 0;
}

/*
Explanation

There are two cases from which you can land on a cell (i,j). Either you were on the cell (i+1,j) or (i+2,j) or (i-1,j) or (i-2,j) or (i,j+1) or (i,j+2) or (i,j-1) or (i,j-2). Now if the island in (i,j) has height k, then the island in the cell from which you jumped on (i,j) must have height k+1. So you have 8 options of where to jump from to land on (i,j). If you have already solved the subproblem when you are at a cell (i,j) with height k, you can use the information stored in that subproblem to calculate the answer for (i,j) with height k+1. For example if you want to calculate the answer for (i,j) with height k+1, you can use the information of dp[i+1][j][k+1], dp[i+2][j][k+1], dp[i-1][j][k+1], dp[i-2][j][k+1], dp[i][j+1][k+1], dp[i][j+2][k+1], dp[i][j-1][k+1], dp[i][j-2][k+1]. So to get the answer for (i,j) with height k, simply sum these 8 numbers modulo 10^9+7 and store it in dp[i][j][k]. You can calculate the answer for the whole final cell like this.
*/
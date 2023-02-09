/*

SAMPLE INPUT 
3
1
0 1
4
1 4
2 4
3 4
4 4
3
1 2
0 0
1 3
SAMPLE OUTPUT 
1
1
5
0000
1
101

Explanation

In the first test case, the only valid solution is that the Bytelandian is a Byteknight.
In the second test case, there are five valid solutions: "0000", "1000", "0100", "0010", and "0001".
In the third test case, there is only one solution: "101".
Time Limit:	2.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Marks are awarded if any testcase passes.
Allowed Languages:	C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, TypeScript, Visual Basic

*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define MOD 1000000007

ll modInverse(ll a, ll m) 
{ 
    ll m0 = m; 
    ll y = 0, x = 1; 
    if (m == 1) 
      return 0; 
    while (a > 1) 
    {
        ll q = a / m; 
        ll t = m;
        m = a % m, a = t; 
        t = y;
        y = x - q * y; 
        x = t; 
    } 
    if (x < 0) 
       x += m0; 
    return x; 
}

ll factorial(ll n)
{
    ll fact = 1;
    for(int i = 1; i <= n; i++)
    {
        fact = (fact*i)%MOD;
    }
    return fact;
}

ll nCr(ll n, ll r)
{
    return (((factorial(n)%MOD)*(modInverse(factorial(r), MOD)%MOD))%MOD*(modInverse(factorial(n-r), MOD)%MOD))%MOD;
}

void solve()
{
    ll n;
    cin >> n;
    ll a[n], b[n];
    ll min = n, max = 0;
    for(int i = 0; i < n; i++)
    {
        cin >> a[i] >> b[i];
        if(a[i] < min)
            min = a[i];
        if(b[i] > max)
            max = b[i];
    }
    ll f = 0;
    for(int i = 0; i < n; i++)
    {
        if(a[i] == min && b[i] == max)
            f++;
    }
    ll val = 0;
    for(int i = max; i >= min; i--)
    {
        val = (val + nCr(i, min))%MOD;
    }
    if(min == max)
        val = 1;
    if(f == n)
        val = 1;
    cout << val << "\n";
    string ans;
    for(int i = 0; i < min; i++)
    {
        ans += '0';
    }
    for(int i = 0; i < max-min; i++)
    {
        ans += '1';
    }
    cout << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        solve();
    }
    return 0;
}
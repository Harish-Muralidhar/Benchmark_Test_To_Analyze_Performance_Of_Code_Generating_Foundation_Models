/*


*/

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

public class _03_YetAnotherGame {
    public static long MOD = 1000000009;
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int tests = in.nextInt();
        for (int test=0;test<tests;test++) {
            int n = in.nextInt();
            int q = in.nextInt();
            int a[] = new int[n];
            for (int i=0;i<n;i++) {
                a[i] = in.nextInt();
            }
            for (int i =0;i<q;i++) {
                long res = 0;
                long m = in.nextLong();
                res = solve(a,n,m);
                System.out.println(res);
            }
        }
    }
    
    public static long solve(int[] a, int n, long m) {
        long res = 0;
        long[] dp = new long[n];
        for (int i=0;i<n;i++) {
            dp[i] = 1;
            for (int j=0;j<i;j++) {
                if (a[i] >= a[j]) {
                    dp[i] += dp[j];
                    dp[i] = dp[i]%MOD;
                }
            }
            res += dp[i];
            res = res%MOD;
        }
        long ans = 1;
        ans =  MOD + res - dp[n-1];
        ans = ans%MOD;
        if (m == 1) return ans;
        long curr = ans;
        for (long i=1;i<m;i++) {
            curr = (curr * ans)%MOD;
        }
        return curr;
    }
}
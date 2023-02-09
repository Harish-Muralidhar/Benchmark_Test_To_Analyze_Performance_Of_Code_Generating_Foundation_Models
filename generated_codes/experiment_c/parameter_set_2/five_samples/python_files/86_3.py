/*


*/

import java.util.Scanner;

public class Main {

    static int n,m;
    static int[][] a;
    static int[][][] dp;
    static int mod = 1000000007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            n = sc.nextInt();
            m = sc.nextInt();
            a = new int[n][m];
            dp = new int[n][m][25];
            int sx = sc.nextInt() - 1;
            int sy = sc.nextInt() - 1;
            int fx = sc.nextInt() - 1;
            int fy = sc.nextInt() - 1;
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    a[i][j] = sc.nextInt();
                }
            }
            System.out.println(solve(sx,sy,a[sx][sy]));
        }
    }

    static int solve(int x, int y, int h){
        if(h == 0){
            return 0;
        }
        if(dp[x][y][h] != 0){
            return dp[x][y][h];
        }
        if(x == n-1 && y == m-1 && h == 1){
            return 1;
        }
        int ans = 0;
        if(x-2 >= 0){
            ans = (ans + solve(x-2,y,h-1))%mod;
        }
        if(x-1 >= 0){
            ans = (ans + solve(x-1,y,h-1))%mod;
        }
        if(x+1 < n){
            ans = (ans + solve(x+1,y,h-1))%mod;
        }
        if(x+2 < n){
            ans = (ans +
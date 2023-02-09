/*

*/

import java.util.Scanner;

public class TestClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T>0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            long a[][] = new long[n][m];
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {
                    a[i][j] = sc.nextLong();
                }
            }
            int turn = 0;
            int count = 0;
            int sum = 0;
            while(n > 0 && m > 0) {
                if(turn == 0) {
                    int minIndex = 0;
                    for(int i=1; i<n; i++) {
                        if(a[i][0] < a[minIndex][0]) {
                            minIndex = i;
                        }
                    }
                    for(int i=0; i<m; i++) {
                        sum += a[minIndex][i];
                    }
                    if(minIndex == 0) {
                        for(int i=1; i<n; i++) {
                            a[i-1] = a[i];
                        }
                        n--;
                    }
                    else {
                        for(int i=minIndex; i<n-1; i++) {
                            a[i] = a[i+1];
                        }
                        n--;
                    }
                }
                else {
                    int minIndex = 0;
                    for(int i=1; i<m; i++) {
                        if(a[0][i] < a[0][minIndex]) {
                            minIndex = i;
                        }
                    }
                    for(int i=0; i<n; i++) {
                        sum += a[i][minIndex];
                    }
                    if(minIndex == 0) {
                        for(int i=0; i<n; i++) {
                            for(int j=1; j<m; j++) {
                                a[i][j-1] = a[i][j];
                            }
                        }
                        m--;
                    }
                    else {
                        for(int i=0; i<n; i++) {
                            for(int j=minIndex; j<m-1; j++) {
                                a[i][j] = a[i][j+1];
                            }
                        }
                        m--;
                    }
                }
                turn = (turn+1)%2;
            }
            System.out.println(sum);
            T--;
        }
    }
}
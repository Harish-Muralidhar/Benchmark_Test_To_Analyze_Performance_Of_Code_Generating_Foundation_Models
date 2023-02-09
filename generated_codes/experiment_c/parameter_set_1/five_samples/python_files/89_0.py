/*

Constraints

Time limit: 0.1s
Memory limit: 32MB

*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class CodechefCode {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) {

        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int[][] arr = new int[m][];
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                arr[i] = new int[4];
                if (st.nextToken().equals("P")) {
                    arr[i][0] = 1;
                    arr[i][1] = Integer.parseInt(st.nextToken());
                    arr[i][2] = Integer.parseInt(st.nextToken());
                } else {
                    arr[i][0] = 2;
                    arr[i][1] = Integer.parseInt(st.nextToken());
                    arr[i][2] = Integer.parseInt(st.nextToken());
                }
            }
            int[] brr = new int[n + 1];
            while (st.hasMoreTokens()) {
                brr[Integer.parseInt(st.nextToken())]++;
            }
            solve(arr, brr);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void solve(int[][] arr, int[] brr) {
        for (int i = 0; i < arr.length; i++) {
            int[] temp = arr[i];
            if (temp[0] == 1) {
                for (int k = temp[1]; k <= temp[2]; k++) {
                    brr[k]++;
                }
            } else {
                for (int k = temp[1]; k <= temp[2]; k++) {
                    brr[k]--;
                }
            }
        }
        for (int i = 0; i < brr.length; i++) {
            System.out.println(brr[i]);
        }
    }
}
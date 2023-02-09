/*

Explanation

Test Case 1: After the first round, the numbering will be [1, 0, 1, 2]

Test Case 2: After the first round, the numbering will be [2, 2, 1, 2, 3, 3]. After the second round, the numbering will be [3, 2, 1, 1, 2, 3].
 */
import java.util.*;
import java.lang.*;
import java.io.*;

public class Soldier_and_Memory_Test {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String[] str = br.readLine().split(" ");
            int n = Integer.parseInt(str[0]);
            int m = Integer.parseInt(str[1]);
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = j;
            }
            int[] loc = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int[] sol = new int[n];
            for (int j = 0; j < m; j++) {
                int loc1 = loc[j];
                int temp = arr[loc1];
                for (int k = loc1 - 1; k >= 0; k--) {
                    arr[k] = arr[k + 1];
                }
                for (int k = loc1 + 1; k < n; k++) {
                    arr[k] = arr[k - 1];
                }
                arr[loc1] = 0;
                for (int k = 0; k < n; k++) {
                    sol[k] = Math.max(sol[k], arr[k]);
                }
            }
            for (int j = 0; j < n; j++) {
                System.out.print(sol[j] + " ");
            }
            System.out.println();
        }
    }
}
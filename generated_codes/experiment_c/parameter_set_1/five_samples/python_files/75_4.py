/*



*/

import java.util.*;
import java.io.*;

public class Main {
	public static void main(String args[]) throws IOException {

		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = sc.nextInt();
		while (t > 0) {
			int n = sc.nextInt();
			int k = sc.nextInt();
			int[] a = new int[n];
			int i = 0;
			for (i = 0; i < n; i++) {
				a[i] = sc.nextInt();
			}
			i = 0;
			while (i < n) {
				if (a[i] == 0) {
					i++;
				} else if (i == n - 1) {
					break;
				} else if (a[i] + k >= a[i + 1]) {
					a[i] = a[i] - a[i + 1] + k;
					a[i + 1] = 0;
					i++;
				} else {
					break;
				}
			}
			if (i == n - 1 && a[n - 1] == 0) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
			t--;
		}

	}
}
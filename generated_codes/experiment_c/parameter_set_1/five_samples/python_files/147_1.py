/*

Explanation
Example case 1. There was only one car moving on the segment. It clearly moved at its maximum speed.

Example case 2. The first car is moving at its maximum speed. It is the only car moving at its maximum speed. The second car is clearly not moving at its maximum speed because it is behind the third car. The third car is moving at its maximum speed.

Example case 3. The first and the last cars are moving at their maximum speed. All other cars are not moving at their maximum speed.

Time Limit:	1.0 sec(s) for each input file.
*/

import java.util.Scanner;
import java.util.Stack;
public class FormingTeams {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int n = sc.nextInt();
			int[] a = new int[n];
			for (int j = 0; j < n; j++) {
				a[j] = sc.nextInt();
			}
			int ans = 0;
			Stack<Integer> s1 = new Stack<Integer>();
			Stack<Integer> s2 = new Stack<Integer>();
			for (int j = 0; j < n; j++) {
				if (s1.isEmpty()) {
					s1.push(a[j]);
				} else if (s1.peek() == a[j] - 1) {
					s1.push(a[j]);
				} else if (s2.isEmpty()) {
					s2.push(a[j]);
				} else if (s2.peek() == a[j] - 1) {
					s2.push(a[j]);
				} else {
					if (s1.size() > s2.size()) {
						if (s1.peek() == s2.peek() + 1) {
							ans += s1.size();
							s2.clear();
							s1.clear();
							s1.push(a[j]);
						} else if (s2.peek() != s1.peek() + 1) {
							ans += s1.size();
							s2.clear();
							s1.clear();
						} else {
							s1.push(a[j]);
						}
					} else {
						if (s2.peek() == s1.peek() + 1) {
							ans += s2.size();
							s2.clear();
							s1.clear();
							s2.push(a[j]);
						} else if (s1.peek() != s2.peek() + 1) {
							ans += s2.size();
							s2.clear();
							s1.clear();
						} else {
							s2.push(a[j]);
						}
					}
				}
			}
			if (s1.size() > s2.size()) {
				ans += s1.size();
			} else {
				ans += s2.size();
			}
			System.out.println(ans);
		}
	}
}
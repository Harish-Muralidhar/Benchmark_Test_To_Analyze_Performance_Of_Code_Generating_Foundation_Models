/*

*/

import java.util.Scanner;
import java.math.BigInteger;

class AddFractions {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T-- > 0) {
			int N = sc.nextInt();
			BigInteger numerator[] = new BigInteger[N];
			BigInteger denominator[] = new BigInteger[N];
			for(int i = 0; i < N; i++) {
				numerator[i] = sc.nextBigInteger();
				denominator[i] = sc.nextBigInteger();
			}
			for(int i = 0; i < N; i++) {
				BigInteger sum = numerator[i];
				BigInteger den = denominator[i];
				for(int j = i + 1; j < N; j++) {
					sum = sum.multiply(denominator[j]).add(numerator[j].multiply(den));
					den = den.multiply(denominator[j]);
					BigInteger gcd = sum.gcd(den);
					sum = sum.divide(gcd);
					den = den.divide(gcd);
				}
				System.out.println(sum + "/" + den);
			}
			if(T != 0)
				System.out.println();
		}
	}
}
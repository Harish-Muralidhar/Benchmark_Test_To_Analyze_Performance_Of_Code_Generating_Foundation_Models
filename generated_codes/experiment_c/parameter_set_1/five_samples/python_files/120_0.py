/*
Required sum = 6.0
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

class FunWithProbability {
    public static void main(String args[] ) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String input[] = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[1]);
            Double[][] matrix = new Double[n][m];
            Arrays.fill(matrix[0], 1.0);
            double sum = m;
            for(int j=1;j<matrix.length;j++){
                matrix[j][0] = 1.0;
                sum++;
                for(int k=1;k<matrix[0].length;k++){
                    matrix[j][k] = 0.5*(matrix[j-1][k]+matrix[j][k-1]);
                    sum += matrix[j][k];
                }
            }
            System.out.printf("%.6f\n",sum);
        }
    }
}
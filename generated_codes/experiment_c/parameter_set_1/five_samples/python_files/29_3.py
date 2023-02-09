/*

*/

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        ArrayList<Double> salaries = new ArrayList<>();

        for (int i = 0; i < T; i++) {
            double salary = input.nextDouble();
            salaries.add(salary);
        }

        for (int i = 0; i < T; i++) {
            double salary = salaries.get(i);
            double HRA = 0;
            double DA = 0;
            if (salary < 1500) {
                HRA = salary * 10 / 100;
                DA = salary * 90 / 100;
            } else {
                HRA = 500;
                DA = salary * 98 / 100;
            }

            double grossSalary = salary + HRA + DA;
            System.out.printf("%.2f\n", grossSalary);
        }
    }
}
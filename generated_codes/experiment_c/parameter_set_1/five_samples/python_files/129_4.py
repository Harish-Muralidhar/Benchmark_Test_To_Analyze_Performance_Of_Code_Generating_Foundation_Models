/*

Explanation

First test case: Suppose the atoms we create are {0}, {1, 2} and {3, 4}. Then each of the Si's is the union of some atoms and x is in some atom for all x in X. Furthermore there are no two atoms that share a common element.


Second test case: Suppose the atoms we create are {0}, {1}, {2} and {3}. Then each of the Si's is the union of some atoms and x is in some atom for all x in X. Furthermore there are no two atoms that share a common element.

**/

import java.util.*;
public class AtomPartition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t>0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int v[] = new int[n];
            for(int j = 0;j<m;j++){
                int size = sc.nextInt();
                for(int i = 0;i<size;i++){
                    v[sc.nextInt()] = 1;
                }
            }
            int count = 0;
            for(int i = 0;i<v.length;i++){
                if(v[i]==1){
                    count++;
                }
            }
            System.out.println(count);
            t--;
        }
    }
}
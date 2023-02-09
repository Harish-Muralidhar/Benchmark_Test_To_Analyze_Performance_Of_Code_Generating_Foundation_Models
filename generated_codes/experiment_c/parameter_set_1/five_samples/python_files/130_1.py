/*




*/
import java.io.*;
import java.util.*;
import java.math.*;
 
class TestClass {
    public static void main(String args[] ) throws Exception {
        Scanner scan = new Scanner(System.in);
        int t=scan.nextInt();
        for(int i=0;i<t;i++){
            String str=scan.next();
            int count=0;
            int max=0;
            if(str.length()==1){
                System.out.println(0);
                continue;
            }
            for(int j=1;j<str.length();j++){
                if(str.charAt(j)=='.'){
                    count++;
                }else{
                    max=Math.max(max,count);
                    count=0;
                }
                
            }
            System.out.println(max);
        }
    }
}
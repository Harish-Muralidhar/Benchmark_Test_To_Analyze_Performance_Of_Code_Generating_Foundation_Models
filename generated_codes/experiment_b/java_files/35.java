"""

"""

import java.util.*;
class factorial_numbers
{
    public static void main (String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int x=0;x<n;x++)
        {
            int a=sc.nextInt();
            int fact=1;
            
            while(a>0)
            {
                fact=fact*a;
                a--;
                
            }
            System.out.println(fact);
            
        }
    }
}
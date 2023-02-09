/*

**/


import java.util.*;
public class BalancedParenthesis
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t>0)
		{
			String s = sc.next();
			int len = s.length();
			int balance = 0;
			int max_balance = 0;
			for(int i=0;i<len;i++)
			{
				char c = s.charAt(i);
				if(c=='(')
				{
					balance = balance + 1;
				}
				else
				{
					balance = balance - 1;
				}
				if(balance > max_balance)
					max_balance = balance;
			}
			String s1 = "";
			for(int i=0;i<max_balance;i++)
			{
				s1 = s1 + "(";
			}
			for(int i=max_balance;i>=0;i--)
			{
				s1 = s1 + ")";
			}
			System.out.println(s1);
			t = t-1;
		}
	}
}
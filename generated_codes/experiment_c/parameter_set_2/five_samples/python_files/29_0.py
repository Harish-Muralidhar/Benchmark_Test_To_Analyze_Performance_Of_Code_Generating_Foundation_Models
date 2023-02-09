/*

*/

#include <stdio.h>

int main(void) {
	// your code goes here
	int t,salary;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d",&salary);
	    if(salary<1500)
	    {
	        salary=salary+0.1*salary+0.9*salary;
	        printf("%d\n",salary);
	    }
	    else
	    {
	        salary=salary+500+0.98*salary;
	        printf("%d\n",salary);
	    }
	}
	return 0;
}
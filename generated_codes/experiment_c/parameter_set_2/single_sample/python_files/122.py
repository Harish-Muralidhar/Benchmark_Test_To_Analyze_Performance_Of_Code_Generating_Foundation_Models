/*

*/

#include <stdio.h>
#include <math.h>

int main()
{
	int t,k,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&k);
		if(k==0)
			printf("3\n");
		else
		{
			printf("3.");
			for(i=0;i<k;i++)
				printf("1");
			printf("\n");
		}
	}
	return 0;
}
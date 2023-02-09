



#include<stdio.h>
int main()
{
	int n,m,q,sx,sy,p1,p2,t,i,j,x,t1,t2,d=0;
	scanf("%d%d%d",&n,&m,&q);
	scanf("%d%d",&sx,&sy);
	int a[n][m];
	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			a[i][j]=0;
		}
	}
	a[sx-1][sy-1]=1;
	for(i=0;i<6;i++)
	{
		scanf("%d%d",&p1,&p2);
		x=i;
		if(x==0)
		{
			t1=n;
			t2=0;
		}
		else if(x==1)
		{
			t1=0;
			t2=m;
		}
		else if(x==2)
		{
			t1=n;
			t2=m;
		}
		else if(x==3)
		{
			t1=m;
			t2=n;
		}
		else if(x==4)
		{
			t1=m;
			t2=0;
		}
		else if(x==5)
		{
			t1=0;
			t2=n;
		}
		for(t=0;t<q;t++)
		{
			scanf("%d",&T);
			d=d+T;
			for(int k=1;k<=T;k++)
			{
				
			}
		}
	}
	return 0;
}
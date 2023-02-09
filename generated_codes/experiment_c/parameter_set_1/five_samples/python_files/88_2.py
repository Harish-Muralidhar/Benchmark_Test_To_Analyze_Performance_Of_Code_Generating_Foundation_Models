/*


*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	// your code goes here
	
	int n,m,q,sx,sy,p1,p2,x,t;
	long long int sum=1;
	scanf("%d %d %d",&n,&m,&q);
	scanf("%d %d",&sx,&sy);
	
	int arr[n][m];
	int arr1[6][2];
	
	for(int i=0;i<6;i++)
	{
	    scanf("%d %d",&p1,&p2);
	    arr1[i][0]=p1;
	    arr1[i][1]=p2;
	}
	
	for(int i=0;i<n;i++)
	{
	    for(int j=0;j<m;j++)
	    {
	        arr[i][j]=0;
	    }
	}
	
	arr[sx-1][sy-1]=1;
	
	while(q!=0)
	{
	    sum=1;
	    scanf("%d",&t);
	    for(int i=0;i<t;i++)
	    {
	        int count1=0,count2=0,count3=0,count4=0;
	        for(int j=0;j<n;j++)
	        {
	            for(int k=0;k<m;k++)
	            {
	                count1=0;
	                count2=0;
	                count3=0;
	                count4=0;
	                if(arr[j][k]==1)
	                {
	                    count1=arr[j][k];
	                    if(j!=0 && arr[j-1][k]==1)
	                    {
	                        count1++;
	                    }
	                    if(j!=n-1 && arr[j+1][k]==1)
	                    {
	                        count1++;
	                    }
	                    if(k!=0 && arr[j][k-1]==1)
	                    {
	                        count1++;
	                    }
	                    if(k!=m-1 && arr[j][k+1]==1)
	                    {
	                        count1++;
	                    }
	                    if(j!=0 && k!=0 && arr[j-1][k-1]==1)
	                    {
	                        count1++;
	                    }
	                    if(j!=0 && k!=m-1 && arr[j-1][k+1]==1)
	                    {
	                        count1++;
	                    }
	                    if(j!=n-1 && k!=0 && arr[j+1][k-1]==1)
	                    {
	                        count1++;
	                    }
	                    if(j!=n-1 && k!=m-1 && arr[j+1][k+1]==1)
	                    {
	                        count1++;
	                    }
	                    
	                    x=count1%6;
	                    if(x==0)
	                    {
	                        count2=0;
	                        count3=0;
	                        count4=0;
	                        for(int a=0;a<m;a++)
	                        {
	                            if((j-arr1[x][0])%arr1[x][0]==0 && arr[j-arr1[x][0]][a]!=1)
	                            {
	                                arr[j-arr1[x][0]][a]=1;
	                                count2++;
	                            }
	                            if((j+arr1[x][1])%arr1[x][1]==0 && arr[j+arr1[x][1]][a]!=1)
	                            {
	                                arr[j+arr1[x][1]][a]=1;
	                                count4++;
	                            }
	                        }
	                        for(int a=0;a<n;a++)
	                        {
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[a][k-arr1[x][0]]!=1)
	                            {
	                                arr[a][k-arr1[x][0]]=1;
	                                count3++;
	                            }
	                            if((j+arr1[x][0])%arr1[x][0]==0 && arr[a][k+arr1[x][1]]!=1)
	                            {
	                                arr[a][k+arr1[x][1]]=1;
	                                count3++;
	                            }
	                        }
	                        sum+=count2+count3+count4;
	                        /*
	                        for(int a=0;a<n;a++)
	                        {
	                            for(int b=0;b<m;b++)
	                            {
	                                printf("%d ",arr[a][b]);
	                            }
	                            printf("\n");
	                        }
	                        printf("\n");
	                        */
	                    }
	                    else if(x==1)
	                    {
	                        count2=0;
	                        count3=0;
	                        count4=0;
	                        for(int a=0;a<m;a++)
	                        {
	                            if((k-arr1[x][0])%arr1[x][0]==0 && arr[j-arr1[x][0]][a]!=1)
	                            {
	                                arr[j-arr1[x][0]][a]=1;
	                                count2++;
	                            }
	                            if((k+arr1[x][1])%arr1[x][1]==0 && arr[j+arr1[x][1]][a]!=1)
	                            {
	                                arr[j+arr1[x][1]][a]=1;
	                                count4++;
	                            }
	                        }
	                        for(int a=0;a<n;a++)
	                        {
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[a][k-arr1[x][0]]!=1)
	                            {
	                                arr[a][k-arr1[x][0]]=1;
	                                count3++;
	                            }
	                            if((j+arr1[x][0])%arr1[x][0]==0 && arr[a][k+arr1[x][1]]!=1)
	                            {
	                                arr[a][k+arr1[x][1]]=1;
	                                count3++;
	                            }
	                        }
	                        sum+=count2+count3+count4;
	                    }
	                    else if(x==2)
	                    {
	                        count2=0;
	                        count3=0;
	                        count4=0;
	                        for(int a=0;a<m;a++)
	                        {
	                            if((j+arr1[x][0])%arr1[x][0]==0 && arr[j+arr1[x][0]][a]!=1)
	                            {
	                                arr[j+arr1[x][0]][a]=1;
	                                count2++;
	                            }
	                            if((j+arr1[x][1])%arr1[x][1]==0 && arr[j+arr1[x][1]][a]!=1)
	                            {
	                                arr[j+arr1[x][1]][a]=1;
	                                count4++;
	                            }
	                        }
	                        for(int a=0;a<n;a++)
	                        {
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[a][k-arr1[x][0]]!=1)
	                            {
	                                arr[a][k-arr1[x][0]]=1;
	                                count3++;
	                            }
	                            if((j+arr1[x][0])%arr1[x][0]==0 && arr[a][k+arr1[x][1]]!=1)
	                            {
	                                arr[a][k+arr1[x][1]]=1;
	                                count3++;
	                            }
	                        }
	                        sum+=count2+count3+count4;
	                    }
	                    else if(x==3)
	                    {
	                        count2=0;
	                        count3=0;
	                        count4=0;
	                        for(int a=0;a<m;a++)
	                        {
	                            if((k+arr1[x][0])%arr1[x][0]==0 && arr[j-arr1[x][0]][a]!=1)
	                            {
	                                arr[j-arr1[x][0]][a]=1;
	                                count2++;
	                            }
	                            if((k+arr1[x][1])%arr1[x][1]==0 && arr[j+arr1[x][1]][a]!=1)
	                            {
	                                arr[j+arr1[x][1]][a]=1;
	                                count4++;
	                            }
	                        }
	                        for(int a=0;a<n;a++)
	                        {
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[a][k-arr1[x][0]]!=1)
	                            {
	                                arr[a][k-arr1[x][0]]=1;
	                                count3++;
	                            }
	                            if((j+arr1[x][0])%arr1[x][0]==0 && arr[a][k+arr1[x][1]]!=1)
	                            {
	                                arr[a][k+arr1[x][1]]=1;
	                                count3++;
	                            }
	                        }
	                        sum+=count2+count3+count4;
	                    }
	                    else if(x==4)
	                    {
	                        count2=0;
	                        count3=0;
	                        count4=0;
	                        for(int a=0;a<m;a++)
	                        {
	                            if((j-arr1[x][0])%arr1[x][0]==0 && arr[j-arr1[x][0]][a]!=1)
	                            {
	                                arr[j-arr1[x][0]][a]=1;
	                                count2++;
	                            }
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[j+arr1[x][1]][a]!=1)
	                            {
	                                arr[j+arr1[x][1]][a]=1;
	                                count4++;
	                            }
	                        }
	                        for(int a=0;a<n;a++)
	                        {
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[a][k-arr1[x][0]]!=1)
	                            {
	                                arr[a][k-arr1[x][0]]=1;
	                                count3++;
	                            }
	                            if((j-arr1[x][0])%arr1[x][0]==0 && arr[a][k+arr1[x][1]]!=1)
	                            {
	                                arr[a][k+arr1[x][1]]=1;
	                                count3++;
	                            }
	                        }
	                        sum+=count2+count3+count4;
	                    }
	                    else if(x==5)
	                    {
	                        count2=0;
	                        count3=0;
	                        count4=0;
	                        for(int a=0;a<m;a++)
	                        {
	                            if((k-arr1[x][0])%arr1[x][0]==0 && arr[j-arr1[x][0]][a]!=1)
	                            {
	                                arr[j-arr1[x][0]][a]=1;
	                                count2++;
	                            }
	                            if((k-arr1[x][1])%arr1[x][1]==0 && arr[j+arr1[x][1]][a]!=1)
	                            {
	                                arr[j+arr1[x][1]][a]=1;
	                                count4++;
	                            }
	                        }
	                        for(int a=0;a<n;a++)
	                        {
	                            if((j-arr1[x][1])%arr1[x][1]==0 && arr[a][k-arr1[x][0]]!=1)
	                            {
	                                arr[a][k-arr1[x][0]]=1;
	                                count3++;
	                            }
	                            if((j-arr1[x][0])%arr1[x][0]==0 && arr[a][k+arr1[x][1]]!=1)
	                            {
	                                arr[a][k+arr1[x][1]]=1;
	                                count3++;
	                            }
	                        }
	                        sum+=count2+count3+count4;
	                    }
	                }
	            }
	        }
	    }
	    
	    printf("%lld\n",sum);
	    for(int i=0;i<n;i++)
	    {
	        for(int j=0;j<m;j++)
	        {
	            arr[i][j]=0;
	        }
	    }
	    arr[sx-1][sy-1]=1;
	    q--;
	}
	return 0;
}
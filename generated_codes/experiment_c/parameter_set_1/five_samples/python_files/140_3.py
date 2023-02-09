/*
 */

#include <stdio.h>
#include<math.h>
#include<stdlib.h>
int main() {
    
    int t;
    long long int *count;

    scanf("%d",&t);
    count = (long long int *) malloc(t*sizeof(long long int));

    long long int i,j,n,temp;
    for(i=0;i<t;i++)
    {
        temp=0;

        scanf("%lld",&n);

        for(j=0;j<=n/2;j++)
        {
            temp=temp+pow(2,j);
        }
        count[i]=temp;

    }
    for(i=0;i<t;i++)
    {
        printf("%lld\n",count[i]%1000000007);
    }
    return 0;
}
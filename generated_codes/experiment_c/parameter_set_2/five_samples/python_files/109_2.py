

#include <stdio.h>
#include <math.h>

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,flag=0;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            if(i%2==0 && n%2==0)
            {
                if(i+n==(int)sqrt(2*i*n))
                {
                    flag=1;
                    break;
                }
            }
        }
        if(flag)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
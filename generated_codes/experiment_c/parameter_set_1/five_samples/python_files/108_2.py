/*

TIME LIMIT:=1 sec

*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef unsigned long long int ulli;

ulli naive_fact(ulli x)
{
    ulli fact=1,i;
    for(i=1;i<=x;i++)
    {
        fact=fact*i;
    }
    return fact;
}

ulli digit_sum(ulli x)
{
    ulli i=0,sum=0;
    while(x>0)
    {
        sum=sum+x%10;
        x=x/10;
    }
    return sum;
}

ulli find_num_of_cards(ulli n)
{
    ulli i,j,k,l,m,num_of_cards=0;

    for(i=1;i<=n;i++)
    {
        j=i;
        l=0;
        while(j>0)
        {
            l++;
            j=j/10;
        }

        k=digit_sum(i);
        m=digit_sum(naive_fact(l));

        if(k==m)
        {
            num_of_cards++;
        }
    }

    return num_of_cards;
}

int main()
{
    ulli t,i,n,num_of_cards;
    scanf("%llu",&t);
    for(i=0;i<t;i++)
    {
        scanf("%llu",&n);
        num_of_cards=find_num_of_cards(n);
        printf("%llu\n",num_of_cards);
    }
    return 0;
}
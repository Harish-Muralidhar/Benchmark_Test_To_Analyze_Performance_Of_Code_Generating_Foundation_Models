/*

Link: http://www.codechef.com/problems/NARUTO

My solution: http://www.codechef.com/viewsolution/6055576

*/

#include <stdio.h>
#include <string.h>

int main()
{
    int i,t,j,k,l,p,n;
    char s[1000001];
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%s",&s);
        l=strlen(s);
        j=0;
        k=1;
        n=0;
        while(j<l)
        {
            if(s[j]=='.')
            {
                n++;
                j=j+k;
                k++;
            }
            else
            {
                j++;
            }
        }
        printf("%d\n",n);
    }
    return 0;
}
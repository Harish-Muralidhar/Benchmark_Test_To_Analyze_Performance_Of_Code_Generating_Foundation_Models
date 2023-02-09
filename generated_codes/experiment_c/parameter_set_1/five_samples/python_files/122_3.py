/*

*/

#include <stdio.h>

int main()
{
    int T, K, i;
    long long int a = 103993, b = 33102;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%d", &K);
        if(K == 0)
            printf("3");
        else
        {
            printf("3.");
            for(i = 1; i <= K; i++)
            {
                a = a % b;
                a = a * 10;
                printf("%lld", (a / b));
            }
        }
        printf("\n");
    }
    return 0;
}
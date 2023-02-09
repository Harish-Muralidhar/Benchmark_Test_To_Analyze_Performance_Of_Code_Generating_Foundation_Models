/*

Explanation

The first system protects houses 1 through 4, and the second system protects houses 3 through 5.

The first bombing is the 3-rd house, which is protected by both systems.

The second bombing is the 3-rd house again, but now it is protected by only the second system.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    int *a = (int *)calloc(n+1, sizeof(int));
    int *b = (int *)calloc(n+1, sizeof(int));
    int *c = (int *)calloc(n+1, sizeof(int));
    int *d = (int *)calloc(n+1, sizeof(int));

    int i, j, k;
    int count = 0;
    int x, y;
    char s[10];
    for(i = 0; i < m; i++)
    {
        scanf("%s", s);
        if(strcmp(s, "P") == 0)
        {
            scanf("%d %d", &x, &y);
            a[x]++;
            b[y]++;
            count++;
        }
        else if(strcmp(s, "M") == 0)
        {
            scanf("%d %d", &x, &y);
            c[x] += y;
        }
        else if(strcmp(s, "B") == 0)
        {
            scanf("%d", &x);
            printf("%d\n", a[x] + d[x]);
        }
    }

    for(i = 1; i <= n; i++)
    {
        a[i] += a[i-1];
        d[i] += d[i-1];
        d[i] += b[i-1];
        d[i] -= c[i];
    }

    return 0;
}
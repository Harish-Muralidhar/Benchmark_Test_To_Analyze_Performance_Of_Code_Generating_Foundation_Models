/*



Explanation

In the first test case, the minimum total bonus is 460$. If we give 140$ to employee 1, 120$ to employee 2, 100$ to employee 3, and 100$ to employee 4, then all the conditions are satisfied. 

In the second test case, the comparisons are inconsistent. If we give 100$ to employee 1, 100$ to employee 2 and 100$ to employee 3, then employee 1 should get at least 10$ more than employee 2, and employee 2 should get at least 10$ more than employee 3. So, employee 1 should get at least 110$ more than employee 3, which is not possible. 

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int t, n, m, l, i, j, c;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d%d", &n, &m, &l);
        int a[n][n];
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                a[i][j] = 0;
            }
        }
        for(i = 0; i < m; i++) {
            scanf("%d%d%d", &j, &c, &l);
            a[j-1][c-1] = l;
        }
        int flag = 0;
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                if(a[i][j] != 0 && a[j][i] != 0) {
                    if(a[i][j] < a[j][i]) {
                        flag = 1;
                        break;
                    }
                }
            }
            if(flag == 1) {
                break;
            }
        }
        if(flag == 1) {
            printf("Inconsistent analysis.\n");
        }
        else {
            int b[n];
            for(i =
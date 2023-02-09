/*
**/

#include <stdio.h>

int main() {
	//code
	int t;
	scanf("%d",&t);
	
	while(t--){
	    int year;
	    scanf("%d",&year);
	    int days[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
	    int day[7] = {0};
	    int i,j;
	    for(i=1900;i<=year;i++){
	        days[2] = 28;
	        if(i%4==0){
	            days[2] = 29;
	        }
	        for(j=1;j<=12;j++){
	            day[(1 + (day[1] + days[j-1])%7)%7]++;
	        }
	    }
	    int ans = 0;
	    for(i=0;i<7;i++){
	        if(day[i]%7==0){
	            ans = i;
	            break;
	        }
	    }
	    int y = ((year-1900)*365 + ((year-1900)/4))%7;
	    int ans2 = (ans + y)%7;
	    // printf("%d %d %d %d %d %d %d\n",day[0],day[1],day[2],day[3],day[4],day[5],day[6]);
	    // printf("%d\n",ans2);
	    char dayname[7][10] = {"sunday","monday","tuesday","wednesday","thursday","friday","saturday"};
	    printf("%s\n",dayname[ans2]);
	}
	return 0;
}
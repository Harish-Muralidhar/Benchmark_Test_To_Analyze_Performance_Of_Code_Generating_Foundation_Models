/*
 */

#include<stdio.h>
#include<math.h>

int main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int n,j;
		scanf("%d",&n);
		int a[n],i=0;
		while(i<pow(2,n)){
			scanf("%d",&j);
			a[i]=j;
			i++;
		}
		int count=0;
		for(i=0;i<n;i++){
			for(j=0;j<pow(2,n);j++){
				if(a[j]==count){
					printf("%d ",a[j]);
					count++;
				}
			}
		}
		printf("\n");
	}
	return 0;
}
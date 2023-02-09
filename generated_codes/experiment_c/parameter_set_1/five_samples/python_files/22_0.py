/*

**/

#include <iostream>
using namespace std;

int main() {
	int test,sum=0,temp;
	cin>>test;
	while(test>0){
	    sum=0;
	    cin>>temp;
	    sum=temp%10;
	    temp=temp/10;
	    while(temp>0){
	        temp=temp/10;
	    }
        sum=sum+temp;
	    cout<<sum<<endl;
	    test--;
	}
	return 0;
}
/*

*/

#include<iostream>
using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    int c=0;
    for(int i=0; i<n; i++){
        int a;
        cin>>a;
        if(a%k==0){
            c++;
        }
    }
    cout<<c;
    return 0;
}
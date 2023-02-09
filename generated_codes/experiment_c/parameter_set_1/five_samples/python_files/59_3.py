/*

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include<bitset>
using namespace std;

typedef long long int ll;

int main()
{

    int t;
    cin>>t;

    while(t--) {
        int n;
        cin>>n;
        int num;
        bitset<64> bs1;
        bitset<64> bs0;
        for(int i=0;i<n;i++) {
            cin>>num;
            bs1|=bitset<64>(num);
        }
        bs0[0]=bs1[0];
        int power=1;
        for(int i=1;i<64;i++) {
            if(bs1[i]==1) {
                bs0[i]=0;
                bs1=bs1>>power;
                bs0=bs0>>power;
                power=1;
            } else {
                bs0[i]=1;
                bs1=bs1>>power;
                bs0=bs0>>power;
                power=1;
                break;
            }
        }

        ll ans=0;
        for(int i=0;i<64;i++) {
            if(bs0[i]==1) {
                ans+=(ll)pow(2,i);
            }
        }

        if(ans>=1000000009) {
            ans=ans%(ll)1000000009;
        }
        cout<<ans<<endl;
    }

    return 0;
}
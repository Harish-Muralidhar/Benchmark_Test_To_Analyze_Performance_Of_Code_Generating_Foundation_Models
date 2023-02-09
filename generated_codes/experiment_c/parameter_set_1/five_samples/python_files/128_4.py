/*

*/

#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        int k;
        cin>>s>>k;
        string res ="";
        int n = s.length();
        if(n<k)
            cout<<"";
        else
        {
            sort(s.begin(),s.end());
            for(int i=0;i<k;i++)
                res+=s[i];
            cout<<res<<endl;
        }
    }
    return 0;
}
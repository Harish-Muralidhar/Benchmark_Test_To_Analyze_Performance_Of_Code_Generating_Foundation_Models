/*

*/

#include<bits/stdc++.h>
#include<string.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int i;
        int j[n];
        int k[n];
        for(i=0;i<n;i++)
        {
            cin>>j[i];
        }
        for(i=0;i<n;i++)
        {
            cin>>k[i];
        }
        int count_a=0;
        int count_b=0;
        int count=0;
        int a[n];
        int b[n];
        int a_ind=0;
        int b_ind=0;
        int diff[n];
        int diff_ind=0;
        int diff_max=0;
        int diff_max_ind;
        for(i=0;i<n;i++)
        {
            if(j[i]<k[i])
            {
                if(count_a>count_b)
                {
                    b[b_ind++] = j[i];
                    count_b++;
                    a[a_ind++] = k[i];
                    count_a++;
                }
                else
                {
                    b[b_ind++] = j[i];
                    count_b++;
                    diff[diff_ind++] = i;
                }
            }
            else
            {
                if(count_a>count_b)
                {
                    diff[diff_ind++] = i;
                }
                else
                {
                    a[a_ind++] = j[i];
                    count_a++;
                    b[b_ind++] = k[i];
                    count_b++;
                }
            }
        }
        for(i=0;i<diff_ind;i++)
        {
            if(count_a-count_b > diff_max)
            {
                diff_max = count_a-count_b;
                diff_max_ind = i;
            }
            if(count_a>count_b)
            {
                a[a_ind++] = j[diff[i]];
                count_a++;
            }
            else
            {
                b[b_ind++] = j[diff[i]];
                count_b++;
            }
        }
        if(count_a-count_b > diff_max)
        {
            diff_max = count_a-count_b;
            diff_max_ind = diff_ind;
        }
        if(diff_max_ind!=0)
        {
            for(i=0;i<diff_max_ind;i++)
            {
                cout<<a[i];
            }
            for(i=diff_max_ind;i<diff_ind;i++)
            {
                cout<<b[i];
            }
        }
        else
        {
            for(i=0;i<a_ind;i++)
            {
                cout<<a[i];
            }
            for(i=0;i<b_ind;i++)
            {
                cout<<b[i];
            }
        }
        cout<<endl;
    }

    return 0;
}
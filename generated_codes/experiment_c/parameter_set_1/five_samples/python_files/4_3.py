

#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n;
        cin>>n;
        int a[n];
        for(int j=0;j<n;j++)
        {
            cin>>a[j];
        }
        int s=0,p=1;
        int count=0;
        for(int k=0;k<n;k++)
        {
            s=a[k];
            p=a[k];
            if(s==p)
            {
                count++;
            }
            for(int l=k+1;l<n;l++)
            {
                s+=a[l];
                p=p*a[l];
                if(s==p)
                {
                    count++;
                }
            }
        }
        cout<<count<<endl;
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n,count=0;
	    cin>>n;
	    int a[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	    }
	    for(int i=0;i<n;i++)
	    {
	        int sum=0,p=1;
	        for(int j=i;j<n;j++)
	        {
	            sum+=a[j];
	            p=p*a[j];
	            if(sum==p)
	            {
	                count++;
	            }
	        }
	    }
	    cout<<count<<endl;
	}
	return 0;
}
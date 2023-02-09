"""

"""
for _ in range(int(input())):
    x=int(input())
    a=int(input())
    b=list(map(int,input().split()))
    c=int(input())
    d=list(map(int,input().split()))
    count=0
    while(a):
        if(x==b[0]):
            count=count+b[1]
            break
        else:
            x=x-b[0]
            count=count+b[1]
            del b[0]
            del b[0]
            a=a-1
    count=count+1
    while(c):
        if(x==d[0]):
            count=count+d[2]-1
            break
        else:
            x=x-d[0]
            if(count>=d[1]):
                count=count+d[2]-d[1]
                del d[0]
                del d[0]
                del d[0]
                c=c-1
            else:
                del d[0]
                del d[0]
                del d[0]
                c=c-1
    print(count)
"""
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long long int x;
        cin>>x;
        long long int b;
        cin>>b;
        long long int *arr=new long long int[2*b];
        for(int i=0;i<b*2;i++)
        {
            cin>>arr[i];
        }
        long long int c;
        cin>>c;
        long long int *arr1=new long long int[3*c];
        for(int i=0;i<c*3;i++)
        {
            cin>>arr1[i];
        }
        long long int count=0;
        while(b)
        {
            if(x==arr[0])
            {
                count=count+arr[1];
                break;
            }
            else
            {
                x=x-arr[0];
                count=count+arr[1];
                arr[0]=0;
                arr[1]=0;
                b--;
            }
        }
        count=count+1;
        while(c)
        {
            if(x==arr1[0])
            {
                count=count+arr1[2]-1;
                break;
            }
            else
            {
                x=x-arr1[0];
                if(count>=arr1[1])
                {
                    count=count+arr1[2]-arr1[1];
                    arr1[0]=0;
                    arr1[1]=0;
                    arr1[2]=0;
                    c--;
                }
                else
                {
                    arr1[0]=0;
                    arr1[1]=0;
                    arr1[2]=0;
                    c--;
                }
            }
        }
        cout<<count<<endl;
    }
}
"""
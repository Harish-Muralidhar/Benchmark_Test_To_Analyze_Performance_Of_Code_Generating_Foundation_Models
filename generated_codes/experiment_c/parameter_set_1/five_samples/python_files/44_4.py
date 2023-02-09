/*


*/


#include<iostream>
#include<string>

using namespace std;

int main()
{
    int t,n;
    string origin;
    cin>>t;
    while(t--)
    {
        cin>>n>>origin;
        int laddu = 0;
        for(int i=0;i<n;i++)
        {
            string s;
            cin>>s;
            if(s == "CONTEST_WON")
            {
                int rank;
                cin>>rank;
                int bonus = 20 - rank;
                if(bonus>0)
                {
                    laddu += 300 + bonus;
                }
                else
                {
                    laddu += 300;
                }
            }
            else if(s == "TOP_CONTRIBUTOR")
            {
                laddu += 300;
            }
            else if(s == "BUG_FOUND")
            {
                int severity;
                cin>>severity;
                laddu += severity;
            }
            else if(s == "CONTEST_HOSTED")
            {
                laddu += 50;
            }
        }
        int m;
        if(origin == "INDIAN")
        {
            m = 200;
        }
        else
        {
            m = 400;
        }
        int ans = laddu / m;
        cout<<ans<<endl;
    }
    return 0;
}
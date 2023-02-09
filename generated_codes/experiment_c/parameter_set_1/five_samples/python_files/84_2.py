/*
*/

#include <iostream>
#include <vector>
using namespace std;

int main() 
{
	long long int tc;
	cin>>tc;
	while(tc--)
	{
		long long int r,c,g;
		cin>>r>>c>>g;
		long long int col=c;
		long long int row=r;
		long long int coins=0;
		vector<long long int> v;
		long long int temp=0;
		while(col>=0)
		{
			temp=0;
			for(long long int i=row;i>=0;i--)
				temp+=i;
			if(coins+temp>g)
			{
				while(coins<g)
				{
					v.push_back(1);
					row--;
					coins++;
				}
				break;
			}
			else
			{
				coins+=temp;
				v.push_back(temp);
				row--;
				col--;
			}
		}
		cout<<v.size()<<endl;
		for(long long int i=0;i<v.size();i++)
			cout<<v[i]<<" ";
		cout<<endl;
	}
	return 0;
}
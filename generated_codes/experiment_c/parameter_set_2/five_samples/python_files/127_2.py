/*
wi are distinct

*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_set>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int n;
        cin >> n;
        vector<string> v;
        for (int i = 0; i < n; i++)
        {
            string temp;
            cin >> temp;
            v.push_back(temp);
        }
        bool flag = false;
        for (int i = 0; i < n; i++)
        {
            if (s.find(v[i]) != string::npos)
            {
                flag = true;
                break;
            }
        }
        if (flag)
        {
            cout << "Tracy" << endl;
        }
        else
        {
            cout << "Teddy" << endl;
        }
    }
    return 0;
}
/*

*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdio.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        vector<int> arr;
        for (int j = 0; j < n; j++)
        {
            int a;
            cin >> a;
            arr.push_back(a);
        }
        sort(arr.begin(), arr.end());
        int count = 0;
        for (int j = 0; j < arr.size(); j++)
        {
            if (arr[j] == 1)
            {
                count++;
            }
        }
        if (count == arr.size())
        {
            cout << count << endl;
        }
        else
        {
            int f = 0;
            int d = 0;
            for (int j = 0; j < arr.size(); j++)
            {
                if (arr[j] != arr[0])
                {
                    f = j;
                    d = arr[j] - arr[0];
                    break;
                }
            }
            int c = f;
            for (int j = f; j < arr.size(); j++)
            {
                if (arr[j] == arr[f])
                {
                    c++;
                }
            }

            int ans = 0;
            int count1 = 0;
            for (int j = f; j < arr.size(); j++)
            {
                if (arr[j] == arr[f])
                {
                    count1++;
                }
                if (count1 == c)
                {
                    count1 = 0;
                    ans++;

                    if (arr[j] != arr[arr.size() - 1])
                    {
                        f = j + 1;
                        c = 0;
                        for (int k = f; k < arr.size(); k++)
                        {
                            if (arr[k] == arr[f])
                            {
                                c++;
                            }
                        }
                        j = f;
                    }
                }
            }

            cout << ans + count << endl;
        }
    }
}
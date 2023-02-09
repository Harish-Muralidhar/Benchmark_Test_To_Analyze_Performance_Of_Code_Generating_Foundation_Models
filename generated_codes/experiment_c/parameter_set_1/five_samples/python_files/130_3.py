/*

*/

#include <iostream>
#include <string>

using namespace std;

//Returns the max number of consecutive dots
int get_size(string s){
    int size = 0;
    int n = s.size();
    int i = 0;
    while(i < n){
        //if the next character is '.', continue else return the size
        if(s[i++] == '.'){
            size++;
        }
        else{
            return size;
        }
    }
    return size;
}

int main()
{
    int n;
    cin>>n;
    while(n-- > 0){
        string s;
        cin>>s;
        int days = 0;
        int i = 0;
        int n = s.size();
        //Iterate till the end of the string
        while(i < n){
            //get size of the consecutive dots if there are any
            int size = get_size(s.substr(i));
            if(size > 0){
                //if there are consecutive dots, increment the number of days
                days++;
                i+=size;
            }
            else{
                //else skip to the next character
                i++;
            }
        }
        cout<<days<<endl;
    }
    return 0;
}
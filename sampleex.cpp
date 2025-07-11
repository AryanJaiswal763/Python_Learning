#include<bits/stdc++.h>
using namespace std;

int main()
{
    vector<int>v={1, 2, 3, 4, 5};
    for(int i=0;i<v.size();i++)
    {
        v[i]%2==0 ? cout<<v[i]<<" is even\n" : cout<<v[i]<<" is odd\n";
    }
}
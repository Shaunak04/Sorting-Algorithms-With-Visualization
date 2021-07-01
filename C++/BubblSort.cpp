//  Explanation: Repeatedly swap the adjacent elements in wrong order
// TIME COMPLEXITY: O(n^2)
// SPACE COMPLEXITY: O(1)
#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    vector<ll> arr = {12,45,90,-12,30,0,24,8}; 
    ll i,j;
    for(i=0;i<arr.size()-1;i++)
    {
        for(j= 0;j<arr.size()-i-1;j++)
        {
            if(arr[j+1]<arr[j])
            {
                iter_swap(arr.begin()+j,arr.begin()+j+1);
            }
        }
    }
    for(auto k:arr)
    {
        cout<<k<<" ";
    }
    return 0;
}
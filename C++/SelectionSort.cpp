// Explanation: While traversing through the array, find the index of next minimum number in the 
// unsorted section, and swap the elements at minimum index and begining of unsorted section
// TIME COMPLEXITY: O(n^2)
// SPACE COMPLEXITY: O(1)

#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main() 
{
    vector<ll> arr = {12,45,90,-12,30,0,24,8};
    ll i,j,min_index;
    for(i=0;i<arr.size();i++)
    {
        min_index = i;
        for(j = i+1;j<arr.size();j++)
        {
            if(arr[min_index]>arr[j])
            {
                min_index = j; //Find index of Minimum element
            }
        }
        //SWAP
        iter_swap(arr.begin() + i, arr.begin() +min_index);
    }
    for(auto k:arr)
    {
        cout<<k<<" ";
    }
	return 0;
}

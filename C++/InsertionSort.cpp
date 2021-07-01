//  Explanation: The array is virtually split into a sorted and an unsorted part.
//  Values from the unsorted part are picked and placed at the correct position in the sorted part.
//  TIME COMPLEXITY: O(n^2)
//  SPACE COMPLEXITY: O(1)
#include<bits/stdc++.h>
#define ll long long

using namespace std;
 
vector<ll> arr = {12,45,90,-12,30,0,24,8};

int main()
{
    ll i,j,key;
    for(i=1;i<arr.size();i++)
    {
        key = arr[i];
        j = i-1;
        while (j>=0 && arr[j]>key)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
    for(auto k:arr)
    {
        cout<<k<<" ";
    }
    return 0;
}
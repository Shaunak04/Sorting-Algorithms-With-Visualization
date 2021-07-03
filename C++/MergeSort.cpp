// EXPLANATION : Divide and Conquer strategy where we recursively split the array into 2 halves
// until it can no more split, then we merge the atomic elements by comparing and placing in sorted order
// TIME COMPLEXITY: O(nlogn)
// SPACE COMPLEXITY: O(n)

#include<bits/stdc++.h>
#define ll long long
using namespace std;

void merge(int arr[], int left, int m, int right) 
{
    int arr1 = m-left+1, arr2 = right-m;
    int L[arr1], R[arr2];
    int i = 0, j = 0, k = left;
    for(i = 0; i<arr1; i++)
    {
      L[i] = arr[left+i];
    }
    for(j = 0; j<arr2; j++)
    {
      R[j] = arr[m+1+j];
    }
    i=0,j=0;
    while(i < arr1 && j<arr2) {
      if(L[i] <= R[j]) {
         arr[k] = L[i];
         i++;
      }else{
         arr[k] = R[j];
         j++;
      }
      k++;
    }
    while(i<arr1) {       
      arr[k] = L[i];
      i++; 
      k++;
    }
    while(j<arr2) {     
      arr[k] = R[j];
      j++; 
      k++;
    }
}


void mergeSort(int arr[], int left, int right) {
   if(left>=right) {
        return;
   }
     int mid = left+(right-left)/2;
      mergeSort(arr, left, mid);
      mergeSort(arr, mid+1, right);
      merge(arr, left, mid, right);
}

int main()
{
    int arr[8] = {12,45,90,-12,30,0,24,8};
    mergeSort(arr,0,7);
    for(auto k:arr)
    {
        cout<<k<<" ";
    }
    return 0;
}

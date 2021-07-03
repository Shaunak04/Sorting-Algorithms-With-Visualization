# EXPLANATION : Divide and Conquer strategy where we recursively split the array into 2 halves
# until it can no more split, then we merge the atomic elements by comparing and placing in sorted order
# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(n)

import time
from colors import *

def merge_sort(arr,drawArray,timer):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L,drawArray,timer)
        merge_sort(R,drawArray,timer)
        
        #Merging 
        i=0
        j=0
        k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        drawArray(arr, [PURPLE if x >= 0 and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=len(arr)-1 else BLUE for x in range(len(arr))])
        time.sleep(timer)
    drawArray(arr, [PURPLE if x >= 0 and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=len(arr)-1 else FINAL_GREEN for x in range(len(arr))])
    
# merge_sort(arr)
# print("sorted",arr)
        
# EXPLANATION : Divide and Conquer strategy where we recursively split the array into 2 halves
# until it can no more split, then we merge the atomic elements by comparing and placing in sorted order
# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(n)

import time
from colors import *
comparison = 0
Timecomplexity = "O(nlogn)"
Spacecomplexity = "O(n)"
define = "Divide and Conquer strategy where we recursively split the array into 2 halves until it can no more split, then we merge the atomic elements by comparing and placing in sorted order"
retarr = [comparison,Timecomplexity,Spacecomplexity,define]

def merge(arr, start, mid, end, drawArray, timer):
    global comparison
    global retarr
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            comparison+=1
            tempArray.append(arr[q])
            q+=1
        elif q > end:
            comparison+=1
            tempArray.append(arr[p])
            p+=1
        elif arr[p] < arr[q]:
            comparison+=1
            tempArray.append(arr[p])
            p+=1
        else:
            comparison+=1
            tempArray.append(arr[q])
            q+=1

    for p in range(len(tempArray)):
        arr[start] = tempArray[p]
        start += 1

def merge_sort(arr, start, end, drawArray, timer):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(arr, start, mid, drawArray, timer)
        merge_sort(arr, mid+1, end, drawArray, timer)

        merge(arr, start, mid, end, drawArray, timer)

        drawArray(arr, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(arr))])
        time.sleep(timer)

    retarr[0] = comparison
    drawArray(arr, [FINAL_GREEN for x in range(len(arr))])
    return retarr
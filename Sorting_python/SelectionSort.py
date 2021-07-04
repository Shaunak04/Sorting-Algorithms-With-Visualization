# Explanation: While traversing through the array, find the index of next minimum number in the 
# unsorted section, and swap the elements at minimum index and begining of unsorted section
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

import time
from colors import *

comparison = 0
Timecomplexity = "O(n^2)"
Spacecomplexity = "O(1)"
define = "While traversing through the array, find the index of next minimum number in the unsorted section, and swap the elements at minimum index and begining of unsorted section"
retarr = [comparison,Timecomplexity,Spacecomplexity,define]

def selection_sort(arr,drawArray,timer):
    global comparison
    global retarr
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                comparison+=1
                min_index = j

        # Swap the found minimum element with 
        # the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        drawArray(arr, [YELLOW if x == min_index or x == i else BLUE for x in range(len(arr))] )
        time.sleep(timer)
    retarr[0] = comparison
    drawArray(arr, [FINAL_GREEN for x in range(len(arr))])
    return retarr

# print("Sorted array: ",selection_sort(arr))
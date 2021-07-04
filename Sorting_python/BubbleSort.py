# Explanation: Repeatedly swap the adjacent elements in wrong order
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)


import time
from colors import *

comparison = 0
Timecomplexity = "O(n^2)"
Spacecomplexity = "O(1)"
define = "Explanation: Repeatedly swap the adjacent elements in wrong order"
retarr = [comparison,Timecomplexity,Spacecomplexity,define]

def bubble_sort(arr,drawArray,timer):
    global comparison
    global retarr
# Traverse through all array elements
    for i in range(0,len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                comparison+=1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawArray(arr,[YELLOW if x == j or x == j+1 else BLUE for x in range(len(arr))])
                time.sleep(timer)

    # After sorting is complete
    retarr[0] = comparison
    drawArray(arr, [FINAL_GREEN for x in range(len(arr))])
    return retarr

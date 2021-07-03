# Explanation: The array is virtually split into a sorted and an unsorted part.
# Values from the unsorted part are picked and placed at the correct position in the sorted part.
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

import time
from colors import *

def insertion_sort(arr,drawArray,timer):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
        drawArray(arr, [YELLOW if x == j or x == i else BLUE for x in range(len(arr))])
        time.sleep(timer)

    drawArray(arr,[FINAL_GREEN for k in range(len(arr))])
# print("Sorted array: ",insertion_sort(arr))
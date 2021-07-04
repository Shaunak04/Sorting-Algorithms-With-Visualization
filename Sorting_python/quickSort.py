# Explanation:  QuickSort is a Divide and Conquer algorithm. 
# It picks an element as pivot and partitions the given array around the picked pivot.
# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(logn)

import time
from colors import *

comparison = 0
Timecomplexity = "O(nlogn)"
Spacecomplexity = "O(logn)"
define = """Explanation:  QuickSort is a Divide and Conquer algorithm. It picks an 
element as pivot and recursively partitions the given array around the picked pivot. Elements are swapped after partition"""
retarr = [comparison,Timecomplexity,Spacecomplexity,define]

def partition(arr, start, end, drawArray, timer):
    global comparison
    i = start + 1
    pivot = arr[start]

    for j in range(start+1, end+1):
        if arr[j] < pivot:
            comparison+=1
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return i-1

def quick_sort(arr, start, end, drawArray, timer):
    global comparison
    global retarr
    if start < end:
        pivot_position = partition(arr, start, end, drawArray, timer)
        quick_sort(arr, start, pivot_position-1, drawArray, timer)
        quick_sort(arr, pivot_position+1, end, drawArray, timer)

        drawArray(arr, [PURPLE if x >= start and x < pivot_position else YELLOW if x == pivot_position
                        else DARK_BLUE if x > pivot_position and x <=end else BLUE for x in range(len(arr))])
        time.sleep(timer)
    retarr[0] = comparison
    drawArray(arr, [FINAL_GREEN for x in range(len(arr))])
    return retarr

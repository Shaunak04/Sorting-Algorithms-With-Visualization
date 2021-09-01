# Explanation:  It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.
# TIME COMPLEXITY: O(n+r)
# SPACE COMPLEXITY: O(n+r)
import time
from colors import *

comparison = "N.A"
Timecomplexity = "O(n+r)"
Spacecomplexity = "O(n+r)"
define = "Explanation:  It works by counting the number of elements having distinct values. Then performing cumulative addition to calculate the position of each element in the output sequence."
retarr = [comparison,Timecomplexity,Spacecomplexity,define]

def counting_sort(arr, drawArray, timer):
    global comparison
    global retarr
    n = max(arr) + 1
    count = [0] * n
    for item in arr:
        count[item] += 1
    
    k = 0
    for i in range(n):
        for j in range(count[i]):
            arr[k] = i
            drawArray(arr, [BLUE for x in range(len(arr))] )
            time.sleep(timer)
            k += 1
    drawArray(arr, [FINAL_GREEN for x in range(len(arr))])
    return retarr

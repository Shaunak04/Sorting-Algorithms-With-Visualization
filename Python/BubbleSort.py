# Explanation: Repeatedly swap the adjacent elements in wrong order
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

arr = [12,45,90,-12,30,0,24,8]

# Traverse through all array elements
for i in range(0,len(arr)-1):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array: ",arr)
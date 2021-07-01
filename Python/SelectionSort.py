# Explanation: While traversing through the array, find the index of next minimum number in the 
# unsorted section, and swap the elements at minimum index and begining of unsorted section
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

arr = [12,45,90,-12,30,0,24,8]

# Traverse through all array elements
for i in range(len(arr)):
    # Find the minimum element in remaining unsorted array
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    # Swap the found minimum element with 
    # the first element
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array: ",arr)
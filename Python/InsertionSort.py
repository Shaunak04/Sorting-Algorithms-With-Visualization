# Explanation: The array is virtually split into a sorted and an unsorted part.
# Values from the unsorted part are picked and placed at the correct position in the sorted part.
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

arr = [12,45,90,-12,30,0,24,8]

for i in range(1,len(arr)):
    temp = arr[i]
    j = i-1
    while j>=0 and arr[j]>temp:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = temp

print("Sorted array: ",arr)
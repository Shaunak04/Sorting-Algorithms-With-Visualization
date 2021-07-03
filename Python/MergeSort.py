# EXPLANATION : Divide and Conquer strategy where we recursively split the array into 2 halves
# until it can no more split, then we merge the atomic elements by comparing and placing in sorted order
# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(n)

arr = [12,45,90,-12,30,0,24,8]

def MergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        
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
    
MergeSort(arr)
print("sorted",arr)
        
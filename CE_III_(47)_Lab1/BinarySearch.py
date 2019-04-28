# Best Case: O(1)
# Worst Case: O(log(N))
# Average Case: O(log(N))

def BinarySearch(arr,n):
    first = 0
    last = len(arr)-1
    found = -1

    while first<=last and found == -1:
        midpoint = (first + last)//2
        if arr[midpoint] == n:
            found = midpoint
        else:
            if n < arr[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found



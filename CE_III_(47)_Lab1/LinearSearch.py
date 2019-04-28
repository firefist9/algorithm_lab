# Best Case: O(1)
# Worst Case: O(N)
# Average Case: O(N)

def LinearSearch(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            found = 1
            break
        else:
            found = 0
    if found == 1:
        return 1
    else:
        return -1



def insertion_sort(ar):
    for j in range(1, len(ar)):
        key = ar[j]
        i=j-1
        while i>=0 and ar[i]>key:
            ar[i+1] = ar[i]
            i -= 1
        ar[i+1] = key
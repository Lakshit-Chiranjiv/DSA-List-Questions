#kth largest element in an array in O(n) time and O(1) space

# Method 1: O(nlogn) time and O(1) space
def kthLargest(arr, k):
    arr.sort()
    return arr[-k]

# Method 2: O(n) time and O(1) space
def kthLargest(arr, k):
    n = len(arr)
    l = 0
    r = n-1
    while l <= r:
        p = partition(arr, l, r)
        if p == k-1:
            return arr[p]
        elif p > k-1:
            r = p-1
        else:
            l = p+1
    return -1

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1
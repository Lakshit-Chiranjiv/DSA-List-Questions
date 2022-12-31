# Reverse an array using recursion

# reversing array using 2 pointer approach recursively
def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseArray(arr, start + 1, end - 1)

# reversing array using single parameter recursively
def reverseArray2(arr, n):
    if n >= len(arr) // 2:
        return
    arr[n], arr[len(arr) - n - 1] = arr[len(arr) - n - 1], arr[n]
    reverseArray2(arr, n + 1)

arr = [1, 2, 3, 4, 5, 6]
print(arr)
reverseArray(arr, 0, 5)
print(arr)
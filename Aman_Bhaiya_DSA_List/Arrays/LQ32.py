
def minOperations(arr, n):
    i = 0
    j = n-1
    count = 0
    while i < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
        elif arr[i] > arr[j]:
            j -= 1
            arr[j] += arr[j+1]
            count += 1
        else:
            i += 1
            arr[i] += arr[i-1]
            count += 1
    return count

# recursive solution
def minOperations(arr, i, j):
    if i >= j:
        return 0
    if arr[i] == arr[j]:
        return minOperations(arr, i+1, j-1)
    elif arr[i] > arr[j]:
        arr[j-1] += arr[j]
        return 1 + minOperations(arr, i, j-1)
    else:
        arr[i+1] += arr[i]
        return 1 + minOperations(arr, i+1, j)

arr = [1, 4, 5, 9, 1]
n = len(arr)
print(minOperations(arr, n))
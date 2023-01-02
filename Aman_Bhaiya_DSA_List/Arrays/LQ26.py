def pairInRotatedSorted(arr, n, x):
    s = 0
    e = n - 1
    i = -1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] > arr[mid + 1]:
            i = mid
            break
        elif arr[mid] < arr[s]:
            e = mid - 1
        else:
            s = mid + 1
    if i == -1:
        i = n - 1

    l = (i + 1) % n
    r = i
    while l != r:
        if arr[l] + arr[r] == x:
            return True
        elif arr[l] + arr[r] > x:
            r = (n + r - 1) % n
        else:
            l = (l + 1) % n
    return False

arr = [11, 15, 6, 8, 9, 10]
n = len(arr)
x = 16
print(pairInRotatedSorted(arr, n, x))